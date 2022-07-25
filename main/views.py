from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    location = 'Port Harcourt'

    if 'location' in request.POST:
        location = request.POST['location']

    appid = '845f351a35bf5fc99a1980396bd32c5c'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':location, 'appid':appid, 'units':'metric'}
    weather = requests.get(url=url, params=PARAMS)
    result = weather.json()
    wind_speed = result['wind']['speed']
    temperature = result['main']['temp']
    humidity = result['main']['humidity']
    pressure = result['main']['pressure']
    long = result['coord']['lon']
    lat = result['coord']['lat']

    appid1 = 'JmuTeAzzMz5mGmtD46C9HPfLIufVBoVs'
    url1 = 'https://www.mapquestapi.com/staticmap/v5/map'
    PARAMS1 = {'key':appid1, 'center':location,'size':'600,400@2x'}
    maps = requests.get(url=url1, params=PARAMS1)

    title = 'Weatherly'
    context = {'title':title, 'wind_speed':wind_speed, 'temperature':temperature, 'humidity':humidity, 'pressure':pressure, 'long':long, 'lat':lat, 'location':location}
    return render(request, 'base.html', context)