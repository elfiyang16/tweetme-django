import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "pages/home.html", context={}, status=200)
    # return HttpResponse("<h1>Hello World</h1>")

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    # tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 122)} for x in qs]
    data = {
      "isUser": False,
      "response": tweets_list
    }
    return JsonResponse(data)

def tweet_create_view(request, *args, **kwargs):
  user = request.user
  if not request.user.is_authenticated:
    user = None
    if request.is_ajax():
      return JsonResponse({}, status=401) #not authorised 
    return redirect(settings.LOGIN_URL)
  form = TweetForm(request.POST or None) #initialise with request data or none
  next_url = request.POST.get("next") or None #get the next field 
  if form.is_valid():
    obj = form.save(commit=False)
    #  do some other thing related to the form before save to db 
    obj.user = user or None #annon user set to None just incase the above is_authenticated is pased
    obj.save()
    if request.is_ajax():
      return JsonResponse(obj.serialize(), status=201)#201 create items
    if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
      return redirect(next_url) 
    form = TweetForm() #init a new empty form 
  if form.errors:
    if request.is_ajax():
      return JsonResponse(form.errors, status=400)
  return render(request, "components/form.html", context={"form": form})
  
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
