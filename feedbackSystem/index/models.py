from django.db import models

class Feedback(models.Model):
    username=models.CharField(max_length=30)
    created_date=models.DateTimeField(auto_now_add=True)
    feedback=models.TextField(max_length=300)

# Create your models here.
