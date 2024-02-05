from django.urls import path
from .views import UserSignup, UserLogin, AdminLogin,UserLogout

app_name = "accounts"

urlpatterns = [
    path('signup/',UserSignup.as_view(),name="signup"),
    path('login/',UserLogin.as_view(),name='login'),
    path('admin_login/',AdminLogin.as_view(),name="admin_login"),
    path('logout',UserLogout.as_view(), name='logout')

]