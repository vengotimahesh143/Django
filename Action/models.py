from django.db import models

# Create your models here.
class Studentform(models.Model):
	s_name=models.CharField(max_length=50)
	s_age=models.IntegerField()
	s_roll=models.CharField(max_length=10)
	s_email=models.EmailField(max_length=100)

	def __str__(self):
		return self.s_name+' '+self.s_roll
class Actors(models.Model):
	a_name=models.CharField(max_length=100)
	a_age=models.IntegerField()
	a_no_movies=models.IntegerField()

	def __str__(self):
		return self.a_name+' '+str(self.a_age)
class Heroin_register(models.Model):
	h_name=models.CharField(max_length=100)
	h_age=models.IntegerField()
	h_email=models.EmailField(max_length=100)
	h_password=models.CharField(max_length=30)
	h_manager=models.CharField(max_length=100)

	def __str__(self):
		return self.h_name
class Contact_complaint(models.Model):
	gender=[('MALE','MALE'),('FEMALE','FEMALE')]
	c_name=models.CharField(max_length=100)
	c_mobileno=models.IntegerField()
	c_email=models.EmailField(max_length=40)
	c_gender=models.CharField(max_length=10,choices=gender)
	c_complaint=models.CharField(max_length=2000)

	def __str__(self):
		return self.c_name

