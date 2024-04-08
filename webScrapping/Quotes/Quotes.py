from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

user_tags = input('Enter the tags name or enter "v" to view tags: ')

all_tags = set()
if user_tags == 'v':
    tag = soup.find_all('a', class_='tag')
    for i in tag:
        print(i.text)
        # print(i.a['href'])

# print(all_tags)

quotes = soup.find_all('span', class_="text")

for quote in quotes:
    quote = quote.text.strip()
    print(quote)