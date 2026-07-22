import requests

response = requests.get('https://icanhazdadjoke.com/',headers={"Accept": "application/json"})

if response.ok:
    # print(response.status_code)
    # print(response.text[:1000])

    json_response = response.json()

    # print(json_response)
    # print(type(json_response))
    print(json_response['joke'])
else:
    print(f"Encountered an error. HTTP status code: {response.status_code}")