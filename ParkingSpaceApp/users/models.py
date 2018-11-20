from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	ulatitude = models.DecimalField(max_digits=9, decimal_places=6)
	ulongitude = models.DecimalField(max_digits=9, decimal_places=6)

	def __str__(self):
		return f'{self.user.username} Profile'

