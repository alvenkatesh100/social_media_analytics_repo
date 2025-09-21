from rest_framework import serializers
from .models import SocialPost
from .managers import SocialPostManager

class SocialPostSerializer(serializers.ModelSerializer):
    sentiment = serializers.SerializerMethodField()
    
    class Meta:
        model = SocialPost
        fields = ['platform', 'post_id', 'content', 'likes', 'comments', 'shares', 'created_at', 'sentiment']
    
    def get_sentiment(self, obj):
        manager = SocialPostManager()
        return manager.sentiment_analysis(obj.post_id)
