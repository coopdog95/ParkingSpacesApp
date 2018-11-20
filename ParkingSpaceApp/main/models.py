from django.db import models

class ParkingSpace(models.Model):

	latitude = models.DecimalField(max_digits=9, decimal_places=6)	
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	available = models.BooleanField(default=True)
	cost = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return ("Space at "+str(self.latitude)+", "+str(self.longitude)+". Available: "+str(self.available))