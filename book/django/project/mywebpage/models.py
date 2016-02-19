from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
	username = models.ForeignKey(User)
	std_id = models.IntegerField(primary_key=True)
	std_name = models.CharField(max_length=20)
	#birthdate = models.DateField()
	province_id = models.IntegerField()
	sch_gpa = models.FloatField()
	admit_year = models.CharField(max_length=8)
	def __unicode__(self):
		return str(self.std_id)

class Subject(models.Model):
	sub_id = models.CharField(max_length=5, primary_key=True)
	sub_name = models.CharField(max_length=40)
	description = models.CharField(max_length=500)
	credit = models.IntegerField()
	def __unicode__(self):
		return str(self.sub_id)

class Enrollment(models.Model):
	std_id = models.ForeignKey(Student)
	sub_id = models.ForeignKey(Subject)
	grade = models.CharField(max_length=1)
	term = models.IntegerField()
	year = models.IntegerField()