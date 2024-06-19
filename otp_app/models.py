from django.db import models
from datetime import timedelta, datetime
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# from django.conf import settings
# import secrets
# Create your models here.

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
    
#     USERNAME_FIELD = ("email")
#     REQUIRED_FIELDS = ["username"]
    
#     def _str__(self):
#         return self.email
    

class OtpToken(models.Model):
    email=models.EmailField(unique=True, )
    name = models.CharField(max_length=10, )
    otp = models.CharField(max_length=6, )
    tp_created_at = models.DateTimeField(auto_now_add=True)
    # otp_expires_at = models.DateTimeField(blank=True, null=True)
    
    
    def __str__(self):
        return self.email
    
    def is_expired(self):
        expiration_time = self.otp_created_at + timedelta(minutes=1)
        return datetime.now() > expiration_time