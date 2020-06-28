from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Notice(models.Model):
	heading = models.CharField(max_length=100)
	subheading = models.TextField(default='')
	description = models.TextField(default='')
	pdf = models.ImageField(upload_to='pdf', default='')
	datePublished = models.DateTimeField(auto_now=True)
	# offer = models.BooleanField(default=False)
