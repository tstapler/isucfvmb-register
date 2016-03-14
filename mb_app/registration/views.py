from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from datetime import date

from .forms import RegisterForm

# Create your views here.
def index(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            return HttpResponseRedirect('/thanks/')
    else:
        form = RegisterForm()

    return render(request, 'registration/index.html', {'year': date.today().year, 'registration': form})

def register(request):
    pass
