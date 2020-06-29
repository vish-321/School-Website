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
	standard = models.IntegerField(choices=YEAR_CHOICES,default=5)
	DIV_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F')
    ]
	divison = models.CharField(max_length=1,choices=DIV_CHOICES,default='A')
	def __str__(self):
		return self.studentname + ' (' + str(self.standard) + ' ' + self.divison + ')' 


class Result(models.Model):
	EXAM_CHOICES = [
        ('unit_test_1', 'Unit test 1'),
        ('unit_test_2', 'Unit test 2'),
        ('semister_1', 'Semister 1'),
        ('unit_test_3', 'Unit test 3'),
        ('unit_test_4', 'Unit test 4'),
        ('semister_2', 'Semister 2'),
    ]
	exam = models.CharField(choices=EXAM_CHOICES,default='Semister 1', max_length=20)
	def __str__(self):
		return self.exam

class Subject(models.Model):
	result = models.ForeignKey(Result, on_delete=models.CASCADE,default='Semister_1')
	name = models.CharField(default='', max_length=15)
	obtained_marks=models.IntegerField(default=0)
	total_marks=models.IntegerField(default=0)
	def __str__(self):
		return self.name