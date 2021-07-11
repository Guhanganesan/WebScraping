import requests

data = requests.get('https://www.javatpoint.com/angular-7-tutorial')
print(data.text[:1000])


