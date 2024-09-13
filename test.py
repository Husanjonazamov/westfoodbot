import requests

BASE_URL = "http://127.0.0.1:8000"

response = requests.post(BASE_URL + "/busket/create", data={
    'food_name': "Taom",
    "user_id": 5884447415,
    'count': 1
})

print(response)
print(response.content)