from django.shortcuts import render,HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .models import Flight
from datetime import datetime
from .forms import FlightForm,FlightSearch
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

# Create your views here.

class Home(View):
    """"Home View - This list all flight from current date time or as request of user"""
    template_name = "flight/flightlist.html"
    form_class = FlightSearch

    def get(self,request):
        date_time = request.GET.get('date_time')
        form = self.form_class
        if date_time:
            flights = Flight.objects.filter(departure__gte=date_time)
            return render(request,self.template_name,{"flights":flights,"form":form})
        flights = Flight.objects.all()
        return render(request,self.template_name,{"flights":flights,"form":form})
    

@method_decorator(staff_member_required,name="dispatch") 
class AddFlight(View):
    """"Add Flight View - Only staff member i.e admin can add the flight"""
    login_url = "accounts:admin_login"
    template_name = "flight/addflight.html"
    form_class = FlightForm

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{"form":form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flight:home'))
        return render(request,self.template_name,{"form":self.form_class})


@method_decorator(staff_member_required,name="dispatch") 
class RemoveFlight(View):
    """"Remove Flight View - Only staff member i.e admin can remove the flight"""
    login_url = "accounts:admin_login"

    def get(self,request,pk):
        data = get_object_or_404(Flight,pk=pk)
        data.delete()
        return HttpResponseRedirect(reverse('flight:home'))
    

