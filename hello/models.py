from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Resume(models.Model):
    email = models.CharField(max_length=200)
    resume_text = models.TextField(blank=True, null=True, max_length=20000)
    when = models.DateTimeField('date created', auto_now_add=True)
