from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone_number, password=None):
        if not email:
            raise ValueError("Email is Required")
        if not username:
            raise ValueError("Username is Required")
        if not first_name:
            raise ValueError("First name is Required")
        if not last_name:
            raise ValueError("Last name is Required")
        if not phone_number:
            raise ValueError("Phone Number is Required")
        if not password:
            raise ValueError("password is Required")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, phone_number, password=None):
        user = self.create_user(email, username, first_name, last_name, phone_number, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(verbose_name="User Name", max_length=255)
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name="Email Address", max_length=60, unique=True)
    phone_number = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'username']

    objects = UserManager

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_permissions(self, permissions, obj=None):
        return True

    def has_module_permissions(self, app_label):
        return True
