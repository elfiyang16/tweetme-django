from django.contrib import admin

# Register your models here.

from .models import Tweet, TweetLike

class TweetLikeAdmin(admin.TabularInline):
    model = TweetLike

class TweetAdmin(admin.ModelAdmin):
  inlines = [TweetLikeAdmin]
  list_display = ["__str__", "user"] #a tuple of field names to display, as columns, on the change list page for the object:
  search_fields = ["content", "user__username", "user__email"]
  class Meta:
    model = Tweet
    
    
admin.site.register(Tweet, TweetAdmin) # Tweet has an admin interface
