from django.db import models
from django.utils import timezone

import hashlib

# Create your models here.
class Data(models.Model):
    # id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    name = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now())
    ipaddress = models.GenericIPAddressField(default="127.0.0.1")
    person_id = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

    def hash_ipaddress(self):
        return hash(self.ipaddress)
