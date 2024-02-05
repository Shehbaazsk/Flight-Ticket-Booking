from django.shortcuts import render,HttpResponsePermanentRedirect
from django.urls import reverse
from .forms import TicketBookingForm
from .models import TicketBooking
from flight.models import Flight
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MyTicket(LoginRequiredMixin,View):
    """" User Ticket View - user can fetch all their booked tickets"""
    login_url = 'accounts:login'
    template_name = 'bookings/mybooking.html'

    def get(self, request):
        if request.user.is_staff:
            tickets = TicketBooking.objects.filter(is_booked=True)
        else:
            tickets = TicketBooking.objects.filter(user_id=request.user,is_booked=True)
        return render(request,self.template_name,{'tickets':tickets})


class TicketBookingView(LoginRequiredMixin,View):
    """"Ticket Booking View -  user can book flight tickets"""
    login_url = 'accounts:login'
    tempate_name = 'bookings/ticketbooking.html'
    form_class = TicketBookingForm

    def get(self,request,flight_id):
        form = self.form_class
        return render(request,self.tempate_name,{'form':form,'flight_id':flight_id})
    
    def post(self,request,flight_id):
        form = self.form_class(request.POST)
        data = request.POST
        print(data)
        flight = Flight.objects.get(pk=flight_id)
        first_name = data['first_name']
        last_name = data['last_name']
        mobile_no = data['mobile_no']
        class_type = data['class_type']
        if class_type == "Economy":
            flight_amount = Flight.objects.get(pk=flight_id).economic_fare
        else:
            flight_amount = Flight.objects.get(pk=flight_id).business_fare
        ticket = TicketBooking.objects.create(user_id=request.user,first_name=first_name,last_name=last_name,\
                                              mobile_no=mobile_no,flight_id=flight,amount=flight_amount)
        return HttpResponsePermanentRedirect(reverse("bookings:confirm_ticket",args=[ticket.id]))
    
class TicketConfirmView(LoginRequiredMixin,View):
    """" Ticket Confirm View -  user can confirm their ticket before booking"""
    login_url = 'accounts:login'
    template_name = "bookings/ticketconfirm.html"

    def get(self,request,ticket_id):
        ticket = TicketBooking.objects.get(pk=ticket_id)
        return render(request,self.template_name,{'ticket':ticket})
    
    def post(self,request,ticket_id):
        ticket = TicketBooking.objects.get(pk=ticket_id)
        ticket.is_booked = True
        ticket.save()
        flight = Flight.objects.get(pk=ticket.flight_id.id)
        flight.available_seats -=1
        flight.save()
        return HttpResponsePermanentRedirect(reverse("bookings:my_tickets"))
    
