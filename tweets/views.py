import random
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "pages/home.html", context={}, status=200)
    # return HttpResponse("<h1>Hello World</h1>")

def tweet_list_view(request, *args, **kwargs):
  qs = Tweet.objects.all()
  tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 122)} for x in qs]
  data = {
    "isUser": False,
    "response": tweets_list
  }
  return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    return json data consumed by JS 
    """
    data = {
      "id": tweet_id,
      # "image_path": obj.image_url
    }
    status = 200
    try:
      obj = Tweet.objects.get(id=tweet_id)
      data["content"] = obj.content
    except: #try block to make it handle unfound id 
      data["message"] = "Not Found"
      status = 404    
    return JsonResponse(data, status=status) # json.dumps content_type='application/json'
