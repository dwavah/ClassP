from django.db import models
from users.models import CustomUser  # Ensure correct import

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    assigned_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Newly added field

    def __str__(self):
        return self.title
