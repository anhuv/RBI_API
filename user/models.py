from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class User(AbstractUser):
    # Delete not use field 
    username = None 
    date_joined = None
    first_name = None
    last_name = None
    # is_active = None
    last_login = None
    is_staff = None
    is_superuser = None

    name = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    email_service = models.EmailField(max_length=100, unique=True, blank=True, null=True) 
    phone = models.CharField(max_length=11, blank=True,null=True)
    adress = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=100) 
    
    
    username = models.CharField(max_length=40, blank=True, null=True)
    
    active = models.IntegerField(blank=True, null=False, default='0')
    reject = models.IntegerField(blank=True, null=False, default='0')
    active_notification = models.IntegerField(blank=True, null=False, default='0')
    other_info = models.IntegerField(blank=True, null=True)
    kind = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField(default=datetime.datetime.now()) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'User' 