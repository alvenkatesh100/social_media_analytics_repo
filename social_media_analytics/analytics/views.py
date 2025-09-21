from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SocialPost
from .serializers import SocialPostSerializer
from .managers import SocialPostManager

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

# Custom API for average engagement per platform
class AverageEngagementAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, platform):
        manager = SocialPostManager()
        avg_engagement = manager.average_engagement(platform)
        return Response({"platform": platform, "average_engagement": avg_engagement})
