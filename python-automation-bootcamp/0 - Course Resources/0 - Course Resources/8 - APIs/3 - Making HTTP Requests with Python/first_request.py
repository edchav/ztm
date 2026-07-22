import requests

response = requests.get('https://icanhazdadjoke.com/')

if response.ok:
    print(response.status_code)
    print(response.text[:1000])
else:
    print(f"Encountered an error. HTTP status code: {response.status_code}")