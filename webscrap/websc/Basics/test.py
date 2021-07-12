import requests

res = requests.get('https://www.javatpoint.com/angular-7-tutorial')
print(res.status_code)
print(res.text[:1000])


