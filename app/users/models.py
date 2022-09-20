from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    hospitals = models.ManyToManyField(  
        'hospitals.Hospital', related_name="users")  

    def __str__(self):
        return self.username
