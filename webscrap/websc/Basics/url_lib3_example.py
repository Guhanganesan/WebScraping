import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.javatpoint.com/angular-7-tutorial')
soup = BeautifulSoup(r.data, 'html')
print(soup.title)
print(soup.title.text)