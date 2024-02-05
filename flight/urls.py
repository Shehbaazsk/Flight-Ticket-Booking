from django.urls import path
from .views import Home, AddFlight, RemoveFlight

app_name = 'flight'

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('add_flight',AddFlight.as_view(), name="add_flight"),
    path('remove_flight/<int:pk>',RemoveFlight.as_view(), name="remove_flight")
]
