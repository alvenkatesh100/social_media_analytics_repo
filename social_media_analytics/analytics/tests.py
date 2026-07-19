from django.test import TestCase

from .models import SocialPost
from .xquik import _tweet_id, _tweet_metrics


class SocialPostManagerTests(TestCase):
    def test_sentiment_analysis_uses_bound_model(self):
        post = SocialPost.objects.create(
            platform='example',
            post_id='positive-post',
            content='This release is excellent.',
        )

        result = SocialPost.objects.sentiment_analysis(post.post_id)

        self.assertEqual(result['post_id'], post.post_id)
        self.assertGreater(result['polarity'], 0)
        self.assertIn('subjectivity', result)

    def test_sentiment_analysis_reports_missing_post(self):
        result = SocialPost.objects.sentiment_analysis('missing')

        self.assertEqual(result, {'error': 'Post with id missing not found.'})

    def test_average_engagement_filters_by_platform(self):
        SocialPost.objects.create(
            platform='example',
            post_id='first',
            content='First',
            likes=3,
            comments=2,
            shares=1,
        )
        SocialPost.objects.create(
            platform='example',
            post_id='second',
            content='Second',
            likes=2,
            comments=1,
            shares=1,
        )
        SocialPost.objects.create(
            platform='other',
            post_id='other',
            content='Other',
            likes=100,
        )

        self.assertEqual(SocialPost.objects.average_engagement('example'), 5)
        self.assertEqual(SocialPost.objects.average_engagement('missing'), 0)


class XquikPayloadTests(TestCase):
    def test_current_engagement_fields_are_imported(self):
        metrics = _tweet_metrics({
            'likeCount': 42,
            'replyCount': 3,
            'retweetCount': 5,
        })

        self.assertEqual(metrics, {
            'likes': 42,
            'comments': 3,
            'shares': 5,
        })

    def test_xquik_ids_cannot_overwrite_another_platform(self):
        self.assertEqual(_tweet_id({'id': '123'}, 'Example'), 'xquik-123')
