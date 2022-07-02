import requests

r = requests.get(url='http://api.open-notify.org/iss-now.json')
r.raise_for_status()
data = r.json()
position = longitude, latitude = tuple(data['iss_position'].values())
print(position)


parameters = {
    'lat': latitude,
    'lng': longitude,
}
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
print(data)