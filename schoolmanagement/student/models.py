from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# Create your models here.
class subject(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=8, null=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    gender_type = (('male', 'male'), ('female', 'female'), ('others', 'others'))
    gender = models.CharField(max_length=100, null=True, choices=gender_type)
    dob = models.DateField(null=True)
    mobile_no = models.CharField(max_length=10, null=True)
    date_joined = models.DateField(null=True)
    roll_type = (('Admin', 'Admin'), ('Teacher', 'Teacher'), ('Student', 'Student'))
    roll = models.CharField(max_length=100, null=True, choices=roll_type)
    blood_group = models.CharField(max_length=100, null=True)
    admission_number = models.IntegerField(null=True)
    standard_type = (('10A', '10A'), ('10B', '10B'), ('9A', '9A'), ('9B', '9B'), ('8A', '8A'), ('8B', '8B'))
    standard = models.CharField(max_length=10, null=True, choices=standard_type)
    Subject = models.ForeignKey(subject, on_delete=models.CASCADE, default=True, null=False)
    image = models.FileField(default=None)
    is_tutor = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    objects = UserManager()

    def __str__(self):
        return str(self.first_name)


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **other_fields):
        """
        Create and save a user with the given email and password. And any other fields, if specified.
        """
        if not email:
            raise ValueError('An Email address must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **other_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **other_fields)


class mark_list(models.Model):
    user = models.CharField(max_length=100, null=True)
    user_id = models.CharField(max_length=100, null=True)
    s1 = models.IntegerField(null=True)
    s2 = models.IntegerField(null=True)
    s3 = models.IntegerField(null=True)
    s4 = models.IntegerField(null=True)
    s5 = models.IntegerField(null=True)

    total = models.IntegerField(null=True)
    percentage = models.CharField(max_length=100, null=True)
    grade = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.percentage


class Attendance(models.Model):
    user_id = models.CharField(max_length=100, null=True)
    student_name = models.CharField(max_length=100, null=True)
    standard = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=100, null=True)
    attendance = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.student_name
