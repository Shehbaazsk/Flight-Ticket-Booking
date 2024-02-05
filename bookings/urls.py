from django.urls import path
from .views import TicketBookingView, TicketConfirmView, MyTicket

app_name = 'bookings'

urlpatterns = [
    path('ticket_booking/<int:flight_id>',TicketBookingView.as_view(),name = 'ticket_booking'),
    path('confirm_ticket/<int:ticket_id>',TicketConfirmView.as_view(), name="confirm_ticket"),
    path("my_tickets/", MyTicket.as_view(), name="my_tickets")
]