from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#unique -> If True, this field must be unique throughout the table.
class Student(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=20)
	std_id = models.IntegerField(primary_key=True, unique=True)
	username = models.ForeignKey(User)
	email = models.EmailField(max_length=255)
	#birthdate = models.DateField()
	sch_gpa = models.FloatField()
	province_id = models.CharField(max_length=30)
	admit_year = models.CharField(max_length=8)
	def __unicode__(self):
		return str(self.std_id)

class Subject(models.Model):
	sub_id = models.CharField(max_length=5, primary_key=True, unique=True)
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
	def __unicode__(self):
		return str(self.std_id)

class Factor(models.Model):
	sub_id = models.CharField(max_length=5, primary_key=True, unique=True)
	subfac_1 = models.CharField(max_length=50)
	subfac_2 = models.CharField(max_length=50)
	subfac_3 = models.CharField(max_length=50)
	def __unicode__(self):
		return str(self.sub_id)