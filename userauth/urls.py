from django.urls import path
from .views import RegistrationView,UsernameValidationView,LoginView,LogoutView,RegistrationView,EmailValidationView,FirstnameValidationView,LastnameValidationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("register",csrf_exempt(RegistrationView.as_view()),name="register"),
    path("username_validation",csrf_exempt(UsernameValidationView.as_view()), name="username_validation"),
    path("login",csrf_exempt(LoginView.as_view()), name="login"),
    path('email_validation',csrf_exempt(EmailValidationView.as_view()),name='email_validation'),
    path('firstname_validation',csrf_exempt(FirstnameValidationView.as_view()),name='firstname_validation'),
    path('lastname_validation',csrf_exempt(LastnameValidationView.as_view()),name='lastname_validation'),
    path("logout",csrf_exempt(LogoutView.as_view()), name="logout"),
    
    ]