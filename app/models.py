from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class UserProfileManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None): # here we are creating normal user 
        if not email:
            raise ValueError("Email is not Valid:-- kindly enter valid email")
        email=self.normalize_email(email) # normalize_email = This work is to convert email characters into lower case
        user=self.model(email=email,first_name=first_name,last_name=last_name)
        user.set_password(password) # in this line are setting a password for the password 

        user.save() # here we are saving the user details
        return user
    def create_superuser(self,email,first_name,last_name,password): # Here we are creating a superuser we can say which have more authentication than normal user
        user = self.create_user(email,first_name,last_name,password) # here we are actually creating the table that we want to see in our table
        user.is_superuser=True # In Django by default superuser is False for activate we need to provide True as Manually
        user.is_staff=True # In Django by default staff is False for activate we need to provide True as Manually
        user.save() # here we are saving the user details 

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=100,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    


