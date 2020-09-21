from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "pages/home.html", context={}, status=200)
    # return HttpResponse("<h1>Hello World</h1>")


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
