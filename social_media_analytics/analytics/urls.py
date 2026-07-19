from django.urls import path
from .views import (
    AverageEngagementAPIView,
    SocialPostDetailView,
    SocialPostListCreateView,
    XquikImportAPIView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('posts/', SocialPostListCreateView.as_view(), name='post-list-create'),
    path('posts/xquik/import/', XquikImportAPIView.as_view(), name='xquik-import'),
    path('posts/<str:post_id>/', SocialPostDetailView.as_view(), name='post-detail'),
    path('posts/<str:platform>/average/', AverageEngagementAPIView.as_view(), name='avg-engagement'),
    
    # JWT endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
