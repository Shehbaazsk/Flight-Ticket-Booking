from django.db import models
from accounts.models import User

# Create your models here.
class Country(models.Model):
    """" Country Model"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    """" State Model"""
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='state')

    def __str__(self):
        return self.name


class City(models.Model):
    """" City Model"""
    name = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='city')

    def __str__(self):
        return self.name

class Flight(models.Model):
    """" Flight Model"""
    plane_name = models.CharField(max_length=150)    #Here we can use foreign key with plane but for simplicity just specifying name 
    origin = models.ForeignKey(City, on_delete=models.PROTECT, related_name="origin")
    destination = models.ForeignKey(City, on_delete=models.PROTECT, related_name="destination")
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    economic_fare = models.FloatField(null=True)
    business_fare = models.FloatField(null=True)
    available_seats = models.PositiveIntegerField(default=60)

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
    class Meta:
        ordering = ['departure']

