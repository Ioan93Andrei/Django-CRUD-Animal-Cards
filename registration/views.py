from django.shortcuts import render, HttpResponseRedirect
# from .models import NormalUser
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
        messages.success(request, 'Account created successfully')  

    else:
        form = UserCreationForm()
    context = {'form': form},
    return render(request, 'register.html', context)