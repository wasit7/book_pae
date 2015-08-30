from django.db import models

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=10)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)

	def __unicode__(self):
		return self.username + "," + self.password + "," + self.firstname + "," + self.lastname