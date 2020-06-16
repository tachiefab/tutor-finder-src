from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=500)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __str__(self):
		return self.name
