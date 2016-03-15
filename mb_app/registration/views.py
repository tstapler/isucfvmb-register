from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from datetime import date
from djqscsv import render_to_csv_response
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import RegisterForm, LoginForm

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

@login_required(login_url='/login')
def return_data(request):
    query_set = Student.objects.all()
    return render_to_csv_response(query_set)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        print("User Authenticating")
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            print("Successful")
            return HttpResponseRedirect('/results')
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'login': form})

