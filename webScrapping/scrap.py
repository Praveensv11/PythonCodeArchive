import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com/Praveensv11/PythonCodeArchive')

soup = BeautifulSoup(r.content, 'html.parser')

for link in soup.findAll('a'):
    print(link.get('href'))
