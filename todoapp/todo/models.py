from django.db import models
# from django.contrib.auth.models import User
from users.models import CustomUser


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='todo_photos/', null=True, blank=True)

    def __str__(self)  :
        return self.title 
    
    class Meta:
        ordering = ['completed']

