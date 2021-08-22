from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.


class User(AbstractUser):
    pass


class Entry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=280, null= False, blank= False)
    date = models.CharField(max_length=255)
    time = models.TimeField()

    def __str__(self):
        return f'{self.owner} / {self.title} / {self.date} - {self.time}'

    
    


