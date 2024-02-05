from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.views import View

# Create your views here.
class UserSignup(View):
    """"User Signup View """
    template_name = 'accounts/signup.html'
    form_class = SignupForm

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{"form": form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("accounts:login"))
        else:
            return render(request, self.template_name, {'form': form})
        
class UserLogin(View):
    """"User Login View """
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{"form": form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)    
                return HttpResponseRedirect(reverse("flight:home"))
        return render(request, self.template_name, {'form': form})

class AdminLogin(View):
    """"Admin Login View """
    template_name = 'accounts/adminlogin.html'
    form_class = LoginForm

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user and user.is_staff:
                login(request, user)    
                return HttpResponseRedirect(reverse("flight:home"))
            else:
                return HttpResponseRedirect(reverse("accounts:login"))
        return render(request, self.template_name, {'form': form})
    
    
class UserLogout(View):
    """"Logout View"""
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("flight:home"))