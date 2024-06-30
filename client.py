import requests

response = requests.post(
    "http://localhost:8000/menu/invoke",
    json = {"input":{"topic": "a cafe"}}
    )

print(response.json()['output']['content'])