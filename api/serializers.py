from rest_framework import serializers
from models import *

# serialized_data = serializers.serialize("json", Wheel)

class WheelSerializer(serializers.ModelSerializer):
	

	class Meta:
		model = Wheel
		fields = ('brand','size', 'price')

class CarSerializer(serializers.ModelSerializer):
	brand = serializers.SerializerMethodField('getBrand')


	def getBrand(self, obj):
		return obj.Brand.name


	class Meta:
		model = Car
		fields = ('brand', 'color')
