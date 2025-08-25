import requests
response = requests.get('http://api.open-notify.org/astros.json')
req = response.json()
for person in req['people']:
    print (person['name'])
