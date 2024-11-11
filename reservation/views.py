from django.shortcuts import render , redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def validation(request):
    return render(request,'reservation/validation.html')


def show(request):
    toutrev=Reservation.objects.all().order_by('date')
    x=toutrev.count()
    return render(request,'reservation/show.html',{'toutrev': toutrev, 'x': x})

def edit(request,id):
    rev=Reservation.objects.get(id=id)
    return render(request,'reservation/edit.html',{'rev':rev})


def update(request,id):
    rev=Reservation.objects.get(id=id)
    if request.method == 'POST':
        form=ReservationForm(request.POST, instance = rev)
        print('hahaha ')
        if form.is_valid():
            form.save()
            print("lala")
            return redirect('/reservation/show')
        else:
            print(form.errors)
    else:
        form = ReservationForm(instance=rev)

    return render(request,'reservation/edit.html',{'rev': rev })


def delete(request, id):
    tabrev=Reservation.objects.get(id=id)
    print(f"Object with ID {id} exists: {tabrev}")
    tabrev.delete()
    return redirect('/reservation/show')

def search(request):
    if request.method == "POST":
        lcin = request.POST.get('username', '')
        try:
            client = Reservation.objects.get(username=username)
            return render(request, 'reservation/show.html', {'client': [client]})
        except client.DoesNotExist:
            message = "not founded: {}".format(username)
            return render(request, 'reservation/show.html', {'message': message})
        except MultipleObjectsReturned:
            clients = client.objects.filter(username=username)
            return render(request, 'reservation/show.html', {'clients': clients})
    else:
        return redirect('/reservation/show')













