from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
#ユーザ情報のDB情報
class UserInfo(models.Model):
    userName = models.CharField(max_length=200)
    country = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title