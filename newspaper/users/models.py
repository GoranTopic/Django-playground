from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.




class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    dick_size = models.PositiveIntegerField(null=True, blank=True)

