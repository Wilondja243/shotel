from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from shotel.app.user.models import User
from shotel.app.user.forms import LoginForm, SignupForm
    

class SignupView(View):
    form_class = SignupForm
    template_name = "user/signup.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        
        if request.method == "POST":
            form = self.form_class(request.POST)

            if form.is_valid():
                user = User(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                )
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.success(request, "Utilisateur crée avec success.")
                return redirect("home")
        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
    template_name = "user/login.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            passowrd = form.cleaned_data['password']

            user = authenticate(request, username=username, password=passowrd)

            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                messages.error(request, "Identifiant incorrect")
        return render(request, self.template_name, {'form': form})
    

class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))
            

    