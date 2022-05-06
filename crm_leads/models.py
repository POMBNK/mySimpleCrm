from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''This Class describes a main atributes for CustomUser model.
     Documentation recomedate to make a AbstractUser inheritance. '''
    pass


class Lead(models.Model):
    '''This Class describes a main atributes for a Lead model and has a dependency 'one to many'. '''
    
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
    source = models.CharField(choices=CHOICES, max_length=100,blank=True)

    profile_picture = models.ImageField(blank=True, null=True)
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    '''This Class describes a main atributes for Agent model and has 'One to One' dependency. '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
