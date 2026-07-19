from requests import RequestException
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SocialPost
from .serializers import SocialPostSerializer
from .xquik import fetch_xquik_posts

# JWT authentication automatically applied from settings

class SocialPostListCreateView(generics.ListCreateAPIView):
    queryset = SocialPost.objects.all()
    serializer_class = SocialPostSerializer
    permission_classes = [permissions.IsAuthenticated]

class SocialPostDetailView(generics.RetrieveAPIView):
    queryset = SocialPost.objects.all()
    serializer_class = SocialPostSerializer
    lookup_field = 'post_id'
    permission_classes = [permissions.IsAuthenticated]


class XquikImportAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        query = str(request.data.get('query', '')).strip()
        if not query:
            return Response({'detail': 'query is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            limit = int(request.data.get('limit', 10))
        except (TypeError, ValueError):
            return Response({'detail': 'limit must be an integer'}, status=status.HTTP_400_BAD_REQUEST)
        limit = max(1, min(limit, 100))

        try:
            rows = fetch_xquik_posts(query, limit=limit)
        except ValueError as exc:
            return Response({'detail': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        except RequestException as exc:
            return Response(
                {'detail': f'Xquik request failed: {exc}'},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        posts = []
        for row in rows:
            post, _created = SocialPost.objects.update_or_create(
                post_id=row['post_id'],
                defaults={
                    'platform': row['platform'],
                    'content': row['content'],
                    'likes': row['likes'],
                    'comments': row['comments'],
                    'shares': row['shares'],
                },
            )
            posts.append(post)

        serializer = SocialPostSerializer(posts, many=True)
        return Response(
            {'query': query, 'imported': len(posts), 'posts': serializer.data},
            status=status.HTTP_201_CREATED,
        )

# Custom API for average engagement per platform
class AverageEngagementAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, platform):
        avg_engagement = SocialPost.objects.average_engagement(platform)
        return Response({"platform": platform, "average_engagement": avg_engagement})
