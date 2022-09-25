from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=300, default='As a new user, kindly update your profile to reflect your bio.')
    

    def __str__(self):
        return f'{self.user.username} Profile'
    
