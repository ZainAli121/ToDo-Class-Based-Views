from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    desc =  models.TextField(null=True, blank=True)
    comeplete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)  # automatically add this field when the object is created

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['comeplete']  # order the tasks by the complete field