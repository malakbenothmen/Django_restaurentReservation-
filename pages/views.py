from django.shortcuts import render , redirect
from food.models import food
from reservation.models import Reservation
from reservation.forms import ReservationForm
from .models import login

# Create your views here.

def index(request):
    return render(request,'pages/index.html')
    

def menu(request):
    return render(request,'pages/menu.html',{'menu': food.objects.all()} )


def about(request):
    return render(request,'pages/about.html')


def reservation(request):
    if request.method == "POST" :
        form= ReservationForm(request.POST)
  
        if form.is_valid():
            try:
                form.save()
                return redirect('/reservation/validation')
            except:
                print("je suis la error")
                pass
    else :
        form = ReservationForm()
        pass

    return render(request,'pages/reservation.html',{'form': form})


def login(request):
    x=request.POST.get('lcin')
    print(x)
    if (x=='admin'):
        return redirect('/reservation/show')

    return render(request,'pages/login.html')
    
