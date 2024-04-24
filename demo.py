#https://requests.readthedocs.io/en/latest/

import requests
import json
import matplotlib.pyplot as plt
from retry_requests import retry

r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m', verify=False)
response_json = r.json()
#for key in response_json:
#    print(key)
time = response_json["hourly"]["time"]
temperature_2m = response_json["hourly"]["temperature_2m"]

print(len(time))
print(len(temperature_2m))
plt.plot(time,temperature_2m)
plt.show()