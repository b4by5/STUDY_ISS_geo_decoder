import requests
from geopy.geocoders import Nominatim

res = requests.get("http://api.open-notify.org/iss-now")

print(res.text)
data = dict(dict(res.json()).items())
lat = dict(data.get('iss_position')).get('latitude')
lng = dict(data.get('iss_position')).get('longitude')
print(f'Координаты МКС: {lat}, {lng}')

try:
    geolocator = Nominatim(user_agent="ISS_locator")
    location = geolocator.reverse(f"{lat}, {lng}")
    print(location.address)
    # print(location.raw)
except AttributeError:
    print('Нет адреса')
