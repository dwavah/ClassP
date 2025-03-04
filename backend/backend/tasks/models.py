from django.db import models
from users.models import CustomUser

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    assigned_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
