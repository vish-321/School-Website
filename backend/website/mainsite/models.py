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
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	year = models.ForeignKey(Year, on_delete=models.CASCADE,default='2018')
	studentname = models.CharField(default='', max_length=50)
	YEAR_CHOICES = [
        (int(5), '5th'),
        (int(6), '6th'),
        (int(7), '7th'),
        (int(8), '8th'),
        (int(9), '9th'),
        (int(10), '10th'),
    ]
	standardname = models.IntegerField(choices=YEAR_CHOICES,default=5)
	DIV_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F')
    ]
	divisonname = models.CharField(max_length=1,choices=DIV_CHOICES,default='A')
	def __str__(self):
		return self.studentname + ' (' + str(self.standardname) + ' ' + self.divisonname + ')' 
