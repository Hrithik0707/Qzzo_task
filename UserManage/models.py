from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from PIL import Image
# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email,password=None):
        if not email:
            raise ValueError('Email must be set!')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    # def get_by_natural_key(self, email):
    #     return self.get(code_number=email)



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField(null=True)
    unique_id = models.CharField(max_length=10,null=True)
    image = models.ImageField(upload_to='pics',null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_by_natural_key(self, email_):
        return self.get(code_number=email_)