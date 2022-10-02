
from urllib import request
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
import json
from django.http import JsonResponse,HttpResponse
from validate_email import validate_email
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import resolve
from django.template import loader





class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email= data['email']

        if not validate_email(email):
            return JsonResponse({"email_error":"Email is invalid"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"email_error":"Email in use please choose another one"}, status=409)
        return JsonResponse({'email_valid':True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data["username"]

        if not str(username).isalnum():
            return JsonResponse({"username_error":"username should only contain alphanumeric characters"},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"username_error":"sorry username in use, choose another one"}, status=409)
        return JsonResponse({"username":True})

class FirstnameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        first_name = data["first_name"]

        if not str(first_name).isalnum():
            return JsonResponse({"firstname_error":"firstname should only contain alphanumeric characters"},status=400)
        if User.objects.filter(first_name=first_name).exists():
            return JsonResponse({"firstname_error":"sorry firstname in use, choose another one"}, status=409)
        return JsonResponse({"firstname":True})

class LastnameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        last_name = data["last_name"]

        if not str(last_name).isalnum():
            return JsonResponse({"lastname_error":"lastname should only contain alphanumeric characters"},status=400)
        if User.objects.filter(last_name=last_name).exists():
            return JsonResponse({"lastname_error":"sorry lastname in use, choose another one"}, status=409)
        return JsonResponse({"lastname":True})




class RegistrationView(View):
    def get(self, request):
        return render(request, 'userauth/registration.html')

    def post(self, request):

    
        username = request.POST.get('username',"defaultValue")
        first_name= request.POST.get('first_name',"defaultValue")
        last_name = request.POST.get('last_name',"defaultValue")
        email = request.POST.get('email',"defaultValue")
        password = request.POST.get('password',"defaultValue")

        

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    return render(request, 'userauth/registration.html')
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email)
            user.set_password(password)
            user.save()
            return render(request, 'userauth/registration.html')




        
        return render(request, 'userauth/registration.html')

class LoginView(View):
    def get(self, request):
        return render(request,"userauth/login.html")

    def post(self,request):

        username = request.POST["username"]
        password = request.POST["password"]

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request,user)
                    
                    return redirect("home")

            
            return render(request,'userauth/login.html')

        
        return render(request,"userauth/login.html")

class LogoutView(View):
    def post (self,request):
        auth.logout(request)
        
        return redirect('login')
        

