from django.shortcuts import render, redirect
from .models import Destination

# Create your views here.

def index(request):
    
    #dest1 = Destination()
    #dest1.name = "Lagos"
    #dest1.img = "destination_1.jpg"
    #dest1.desc = "The happening city"
    #dest1.price = 600
    #dest1.offer = True

    #dest2 = Destination()
    #dest2.name = "Tokyo"
    #dest2.img = "destination_2.jpg"
    #dest2.desc = "The Yin and Yang"
    #dest2.price = 450
    #dest2.offer = False

    #dest3 = Destination()
    #dest3.name = "Paris"
    #dest3.img = "destination_3.jpg"
    #dest3.desc = "The City of Light"
    #dest3.price = 600
    #dest3.offer = False

    dests = Destination.objects.all()
    #dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests':dests})

def destination(request, nme=None, id=None):
    # dests = Destination.objects.
    if id != None:
        dest = Destination.objects.get(id=id)
        # print(dest.name)
        return render(request, 'destination.html', {
            'dest': dest
        })
    return redirect('/')