from django.db import models
from accounts.models import User
from flight.models import Flight

# Create your models here.

### Here we can alos integrate payment gateway but for simpllicity I'm not doing ###

class TicketBooking(models.Model):
    class ClassType(models.TextChoices):
        BUSINESS = 'Business'
        ECONOMY = 'Economy'
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    mobile_no = models.CharField(max_length=12)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    class_type = models.CharField(max_length=20, choices=ClassType.choices)
    is_booked = models.BooleanField(default=False)
    amount = models.DecimalField(decimal_places=2,max_digits=20)

    def __str__(self):
        return f"{self.id} - {self.is_booked}"
