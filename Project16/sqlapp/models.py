from django.db import models

class Employee(models.Model):
	name=models.CharField(max_length=15)
	age=models.IntegerField()
	address=models.CharField(max_length=50)