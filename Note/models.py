from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager, PermissionsMixin
# Create your models here.
from site import check_enableusersite


class MyUserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_field):
        if not username:
            raise ValueError("username must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, password=password, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email, password, **extra_field):
        self.is_active = True
        return self._create_user(username, email, password, **extra_field)

    def create_superuser(self, username, email, password, **extra_field):
        self.is_active = True
        self.is_staff = True
        self.is_superuser = True
        return self._create_user(username, email, password, **extra_field)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=32,unique=True)
    email = models.EmailField(verbose_name="email address", unique=True)
    password = models.CharField(max_length=32)
    date_join = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    object = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username


class Note(models.Model):
    # 笔记表
    fold = models.ForeignKey('Fold',on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    content = models.TextField()
    update_date = models.DateTimeField(auto_now_add=True)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fold

def file_path(instance, filename):
    return 'attachment/{0}/{1}'.format(instance.note, filename)


class File(models.Model):
    #附件表
    note = models.ForeignKey('Note', on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_path)

    def __str__(self):
        return self.file


class Fold(models.Model):   #Check if name exists
    #文件夹表
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name