import requests

sample = {
    "rooms": 3,
    "size": 100,
    "latitude": -23.5505,
    "longitude": -46.6333
}

url = "http://localhost:9696/predict"
response = requests.post(url, json=sample)
print(response.json())

