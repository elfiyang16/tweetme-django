import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url
from .serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


ALLOWED_HOSTS = settings.ALLOWED_HOSTS
# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "pages/home.html", context={}, status=200)
    # return HttpResponse("<h1>Hello World</h1>")
    
@api_view(["GET"])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    username = request.GET.get('username') # ?username=Justin
    if username != None:
        qs = qs.filter(user__username__iexact=username)
    serializer = TweetSerializer(qs, many=True)
    return Response( serializer.data, status=200)
  

@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)
  
@api_view(['DELETE', "POST"])
@permission_classes([IsAuthenticated]) 
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
      return Response({"message": "not authorised"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Tweet removed"}, status=200)

@api_view([ "POST"])
@permission_classes([IsAuthenticated]) 
def tweet_action_view(request, *args, **kwargs):
    '''
    id is required
    like, unlike, retweet
    '''
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      data = serializer.validated_data
      tweet_id = data.get("id")
      action = data.get("action")
      content = data.get("content")

      qs = Tweet.objects.filter(id=tweet_id)
      if not qs.exists():
          return Response({}, status=404)
      obj = qs.first()
      if action == "like":
        obj.likes.add(request.user)
        serializer = TweetSerializer(obj)
        Response(serializer.data, status=200)
      elif action == "unlike": 
        obj.likes.remove(request.user) 
        serializer = TweetSerializer(obj)
        return Response(serializer.data, status=200)
      elif action == "retweet":
        new_tweet = Tweet.objects.create(
                user=request.user, 
                parent=obj,
                content=content,
                )
        serializer = TweetSerializer(new_tweet)
        return Response(serializer.data, status=201)
      # if request.user in obj.likes.all():
    return Response({}, status=200)
  
    
@api_view(["POST"])
# @authentication_classes([SessionAuthentication, MyCustomAuth]) default
@permission_classes([IsAuthenticated]) #check if authenticated or the below function fails to run
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)
  
def tweet_create_view_pure_django(request, *args, **kwargs):
  '''
  change to django rest framework
  '''
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
  
  
def tweet_detail_view_pure_django(request, tweet_id, *args, **kwargs):
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

  
def tweet_list_view_pure_django(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    # tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 122)} for x in qs]
    data = {
      "isUser": False,
      "response": tweets_list
    }
    return JsonResponse(data)