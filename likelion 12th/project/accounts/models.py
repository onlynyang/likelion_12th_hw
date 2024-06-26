from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    department = models.TextField(null=True, max_length=30)
    birth = models.TextField(null=True, max_length=10)
    followings = models.ManyToManyField("self", related_name="followers", symmetrical=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwarags):
    instance.profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwarags):
    instance.profile.save()