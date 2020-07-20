from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.
class User(AbstractUser):
    is_coach = models.BooleanField(default=False)

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    school = models.CharField(max_length=20)
    position = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse()