import requests

url = "https://api.tomorrow.io/v4/timelines"

querystring = {"location":"52.48567329352747, 13.481280612759955",
 "fields": ["temperature","cloudCover"],
 "units":"metric",
 "timesteps":"1d",
 "apikey":"zLP3A82HHv71reOowhrvNL0l4BaRqFVo"}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)
results = response.json()['data']['timelines'][0]['intervals']

print("Weather Forecast for that corner Trepti/Plänti")
print("================")

for result in results:
    date = result['startTime'][0:10]
    temp = round(result['values']['temperature'])
    print("On",date,"it will be", temp, "C")
