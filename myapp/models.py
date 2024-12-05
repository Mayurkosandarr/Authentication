from django.db import models
from django.contrib.auth.models import User

# class Item(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

from django.db import models
from django.utils import timezone

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)  # This will auto-update every time the object is saved
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

