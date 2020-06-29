from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Notice(models.Model):
	marqueeHeading = models.CharField(max_length=50, default='')
	heading = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='pdf', default='')
	datePublished = models.DateTimeField()
	# offer = models.BooleanField(default=False)
	def __str__(self):
		return self.heading

class School(models.Model):
	name = models.CharField(max_length=50, default='')
	
	def __str__(self):
		return self.name

class Year(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE)
	yearname = models.CharField(max_length=10, default='')
	def __str__(self):
		return self.yearname

class Standard(models.Model):
	YEAR_CHOICES = [
        (5, '5th'),
        (6, '6th'),
        (7, '7th'),
        (8, '8th'),
        (9, '9th'),
        (10, '10th'),
    ]
	standardname = models.IntegerField(choices=YEAR_CHOICES,default=5)
	year = models.ForeignKey(Year, on_delete=models.CASCADE)
	def __str__(self):
		return self.standardname

class Div(models.Model):
	standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
	DIV_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F')
    ]
	divname = models.CharField(max_length=1,choices=DIV_CHOICES,default='A')
	def __str__(self):
		return self.divname


