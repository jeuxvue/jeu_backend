from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from main.views import GamesList
from .models import UserRegistrationForm
from django.urls import path, reverse
from rest_framework.response import Response


@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        # print(user_form.errors)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            user_form.save()

            return redirect('successful-registered')
    else:
        user_form = UserRegistrationForm()

    return redirect('redirect-to-register-page')

