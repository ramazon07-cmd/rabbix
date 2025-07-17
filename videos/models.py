from django.conf import settings
from django.db import models

class Video(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='videos/')
    status = models.CharField(max_length=50, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
