from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=1000)

	def __str__(self):
		return self.name + self.description

class Photo(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)