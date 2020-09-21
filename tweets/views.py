from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Tweet
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello World</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(args, kwargs)
    try:
      obj = Tweet.objects.get(id=tweet_id)
    except: #try block to make it handle unfound id 
      raise Http404
    return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>")