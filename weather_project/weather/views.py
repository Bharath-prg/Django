import re

from django.shortcuts import render
import requests

API_KEY='a9120dcad2657dceea36f554a9a81e70'

# Create your views here.
def home(request):
    weather_data=None
    error=None

    if request.method=='POST':
        city=request.POST.get('city')
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response=requests.get(url)

        weather=response.json()

        if response.status_code == 200:
            weather_data={
                'city': weather["name"],
                'temp': weather["main"]["temp"],
                'desc': weather["weather"][0]["description"]
            }
        else:
            error={
                'msg': "enter correct city name"
            }
    return render(request,'home.html',{'weather' : weather_data, 'errors':error})
