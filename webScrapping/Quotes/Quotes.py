from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
quotes = soup.find_all('span', class_="text")

for quote in quotes:
    quote = quote.text.strip()
    print(quote)