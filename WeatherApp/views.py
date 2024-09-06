from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import requests
import datetime



def Home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Malappuram'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e12edc2aa92633f24263454fadb5bd5c'
    PARAMS = {'units' : 'metric'}
    try:
        data = requests.get(url,params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()



        return render(request, "WeatherHome.html", {'temp': temp, 'city': city, 'description': description, 'icon': icon, 'day': day,'city':city ,'exception_occurred':False,})

    except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          day = datetime.date.today()

          return render(request,'WeatherHome.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'Malappuram' , 'exception_occurred':exception_occurred } )