from django.db import models
from django.contrib.auth.models import User

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    liked = models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    
    def __str__(self):
        return self.title
    
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',max_length=10)
    
    def __str__(self):
        return str(self.post)