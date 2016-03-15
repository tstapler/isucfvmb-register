from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from django.contrib import messages
from datetime import date

from .forms import RegisterForm

# Create your views here.
def index(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration Completed Successfully!")
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/index.html', {'year': date.today().year, 'registration': form})

def view_registered(request):
    return render(request, 'registration/registered.html')

def return_data(request):
    pass
