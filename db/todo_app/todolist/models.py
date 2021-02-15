from django.db import models


class Todo(models.Model):
    title=models.CharField(max_length=80)
    complete=models.CharField(max_length=80,default="Pending")
    date=models.DateTimeField(auto_now_add=True)