import hashlib
import os

import requests

XQUIK_SEARCH_URL = 'https://xquik.com/api/v1/x/tweets/search'


def _as_int(value):
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def _rows_from_payload(payload):
    if not isinstance(payload, dict):
        return []
    rows = payload.get('data') or payload.get('tweets') or payload.get('results') or []
    if isinstance(rows, dict):
        return list(rows.values())
    return rows if isinstance(rows, list) else []


def _tweet_text(row):
    return str(
        row.get('text')
        or row.get('content')
        or row.get('full_text')
        or row.get('rawContent')
        or ''
    ).strip()


def _tweet_id(row, text):
    explicit_id = row.get('id') or row.get('tweet_id') or row.get('rest_id')
    if explicit_id:
        return f'xquik-{explicit_id}'
    digest = hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]
    return f'xquik-{digest}'


def _tweet_metrics(row):
    metrics = row.get('metrics') if isinstance(row.get('metrics'), dict) else row
    return {
        'likes': _as_int(
            metrics.get('likeCount')
            or metrics.get('likes')
            or metrics.get('like_count')
        ),
        'comments': _as_int(
            metrics.get('replyCount')
            or metrics.get('replies')
            or metrics.get('reply_count')
        ),
        'shares': _as_int(
            metrics.get('retweetCount')
            or metrics.get('retweets')
            or metrics.get('retweet_count')
        ),
    }


def fetch_xquik_posts(query, limit=10):
    api_key = os.getenv('XQUIK_API_KEY', '')
    if not api_key:
        raise ValueError('XQUIK_API_KEY is required')

    clean_query = (query or '').strip()
    if not clean_query:
        raise ValueError('query is required')

    bounded_limit = max(1, min(int(limit or 10), 100))
    response = requests.get(
        XQUIK_SEARCH_URL,
        params={'q': clean_query, 'limit': bounded_limit},
        headers={'X-API-Key': api_key, 'Accept': 'application/json'},
        timeout=30,
    )
    response.raise_for_status()

    posts = []
    for row in _rows_from_payload(response.json()):
        if not isinstance(row, dict):
            continue
        text = _tweet_text(row)
        if not text:
            continue
        metrics = _tweet_metrics(row)
        posts.append({
            'platform': 'xquik',
            'post_id': _tweet_id(row, text),
            'content': text,
            'likes': metrics['likes'],
            'comments': metrics['comments'],
            'shares': metrics['shares'],
        })
        if len(posts) >= bounded_limit:
            break
    return posts
