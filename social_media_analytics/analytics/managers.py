from django.db import models
from textblob import TextBlob

class SocialPostManager(models.Manager):

    def sentiment_analysis(self, post_id):
        try:
            post = self.get(post_id=post_id)
            blob = TextBlob(post.content)
            return {
                "post_id": post_id,
                "polarity": blob.sentiment.polarity,
                "subjectivity": blob.sentiment.subjectivity
            }
        except self.model.DoesNotExist:
            return {"error": f"Post with id {post_id} not found."}

    def average_engagement(self, platform):
        posts = self.filter(platform=platform)
        if not posts.exists():
            return 0
        total_engagement = sum([p.likes + p.comments + p.shares for p in posts])
        return total_engagement / posts.count()
