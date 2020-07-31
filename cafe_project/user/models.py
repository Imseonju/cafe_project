from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10, null=True, blank=True) #null 정의가 안 되있다. blank 데이터 비었다라고 명시
    birth_day = models.DateField(default=timezone.now, null=True, blank=True)
