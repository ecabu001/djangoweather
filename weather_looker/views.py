from django.shortcuts import render

# Create your views here.
# OWM API url: http://api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={your api key}
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + ",us&appid=a7625b89a286378de99727c7b3a087d0")
        try:
            # test api response and set as json if successful
            my_json_data = api_request.json()
        except Exception as e:
            my_json_data = "Error..."

        # set the api request results as JSON
        my_json_data = api_request.json()

        # Create list of variables to display on web page
        city_conditions = my_json_data['weather'][0]['main']
        city_humidity = my_json_data['main']['humidity']
        city_temp = my_json_data['main']['temp']
        city_temp_C = round(((int(city_temp)) - 273.15),3)
        city_temp_F = round((((int(city_temp) -273.15)*(9/5))+32),3)
        city_name = my_json_data['name']

        # Create dictionary for the varibles
        weather_dict = {
            'zipcode': zipcode,
            'my_json_data': my_json_data,
            'city_name' : city_name,
            'city_conditions': city_conditions,
            'city_temp_C': city_temp_C,
            'city_temp_F': city_temp_F,
            'city_humidity': city_humidity
        }

        return render(request, 'home.html', weather_dict)

    else:
        greeting_string = "Enter a US zipcode to get started"
        return render(request, 'home.html', {'greeting_string': greeting_string})


def about(request):
    return render(request, 'about.html', {})
