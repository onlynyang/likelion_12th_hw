from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=30, null=True)
    writer = models.CharField(max_length=30, null=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]

# Create your models here.
