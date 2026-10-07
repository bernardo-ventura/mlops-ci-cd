import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={"features": [5.1, 3.5, 1.4, 0.2]},
)
response.raise_for_status()
print(response.json())
