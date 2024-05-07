from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    writer = models.CharField(max_length=30)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
