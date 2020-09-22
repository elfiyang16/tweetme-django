from django.db import models
from django.conf import settings
import random
# Create your models here.

User = settings.AUTH_USER_MODEL #build in user model
class Tweet(models.Model):
  #  hidden column: id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE) #many tweets to one user 
  content = models.TextField(blank=True, null=True)
  image = models.FileField(upload_to="images/", blank=True, null=True) #can be blank, and null
  # def __str__(self):
    #     return self.content
  class Meta:
    ordering = ["-id"]
  def serialize(self):
    return {
      "id": self.id,
      "content": self.content,
      "likes": random.randint(0,120)    
    }