from rest_framework import serializers
from django.conf import settings

from .models import Tweet
MAX_TWEET_LENGTH = settings. MAX_TWEET_LENGTH


# The serializers in REST framework work very similarly to 
#  Django's Form and ModelForm classes
class TweetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tweet
    fields = ["content"]
  
  def validate_content(self, value):
    if len(value) > MAX_TWEET_LENGTH:
        raise self.ValidationError("This tweet is too long")
    return value