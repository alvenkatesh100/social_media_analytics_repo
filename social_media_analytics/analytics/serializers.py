from rest_framework import serializers

from .models import SocialPost


class SocialPostSerializer(serializers.ModelSerializer):
    sentiment = serializers.SerializerMethodField()

    class Meta:
        model = SocialPost
        fields = ['platform', 'post_id', 'content', 'likes', 'comments', 'shares', 'created_at', 'sentiment']

    def get_sentiment(self, obj):
        return SocialPost.objects.sentiment_analysis(obj.post_id)
