from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Notice(models.Model):
	marqueeHeading = models.CharField(max_length=50, default='')
	heading = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='pdf', default='')
	datePublished = models.DateTimeField(auto_now=True)
	# offer = models.BooleanField(default=False)
