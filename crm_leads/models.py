from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # phone_number = models.CharField(max_length=11)
    pass


class Lead(models.Model):
    
    CHOICES = (
        ("VK", "VK"),
        ("YouTube", "YouTube"),
        ("Instagram", "Instagram"),
        ("Twitter", "Twitter"),
    )


    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=CHOICES, max_length=100)

    profile_picture = models.ImageField(blank=True, null=True)
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
