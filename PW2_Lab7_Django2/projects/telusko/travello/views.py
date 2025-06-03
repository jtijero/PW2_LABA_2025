from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

  dest1 = Destination()
  dest1.name = "Mumbai"
  dest1.desc = 'The City that Never Sleeps'
  dest1.img = 'destination_1.jpg'
  dest1.price = 700

  dest2 = Destination()
  dest2.name = "Hyderabad"
  dest2.desc = 'First Bityani, Then Sherwani'
  dest2.img = 'destination_2.jpg'
  dest2.price = 650

  dest3 = Destination()
  dest3.name = "Bengaluru"
  dest3.desc = 'Beautiful City'
  dest3.img = 'destination_3.jpg'
  dest3.price = 750

  dest4 = Destination()
  dest4.name = "Miami Beach"
  dest4.desc = 'The City that Never Sleeps too'
  dest4.img = 'destination_4.jpg'
  dest4.price = 780

  dests =[dest1,dest2,dest3,dest4]

  return render(request,"index.html",{'dests': dests})