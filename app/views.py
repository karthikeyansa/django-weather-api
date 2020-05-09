from django.shortcuts import render
import requests
from django.http import HttpResponse
from .forms import City
def index(request):
	if request.method == 'POST':
		form = City(request.POST)
		if form.is_valid():
			url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=ba7bb2fcd4d0e41b8155727a76289e9f'
			city = request.POST['name']
			r = requests.get(url.format(city)).json()
			city_weather = {
			'city' : r['name'],
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon'],
			}
			form = City()
			context = {'city_weather' : city_weather,'form':form}
			return render(request,'weather/index.html',context)
	else:
		form = City()
		context = {'form' : form}
		return render(request,'weather/index.html',context)