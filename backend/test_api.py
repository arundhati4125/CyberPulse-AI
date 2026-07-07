import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "features": [
        0,
        1,
        2,
        181,
        5450,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        9,
        9,
        0,
        0,
        0,
        0,
        1,
        0,
        0.11,
        9,
        9,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0
    ]
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())