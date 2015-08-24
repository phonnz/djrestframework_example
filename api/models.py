from django.db import models

class Wheel(models.Model):

	brand = models.CharField(max_length = 25)
	size = models.CharField(max_length=20)
	price = models.IntegerField(default=100)
	def __unicode__(self):
		return self.brand + ' - ' + self.size

class Car(models.Model):

	Brand = models.ForeignKey('Brand')
	Wheels = models.ForeignKey('Wheel')
	color = models.CharField(max_length=25)
    
	def __unicode__(self):
		return self.Brand.name + ' - ' + self.color

class Brand(models.Model):

	name = models.CharField(max_length=50)
    
	def __unicode__(self):
		return self.name 

   