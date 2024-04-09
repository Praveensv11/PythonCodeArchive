from bs4 import BeautifulSoup
import requests

url = 'https://quotes.toscrape.com/'
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

all_tags = set()
while True:
    user_tags = input('Enter the tags name or enter "v" to view tags: ')

    if user_tags == 'v':
        tag = soup.find_all('a', class_='tag')
        for i in tag:
            all_tags.add(i.text)
        print(all_tags)
    elif user_tags in all_tags:
        print('done')
        break


# quotes = soup.find_all('span', class_="text")

# for quote in quotes:
#     quote = quote.text.strip()
#     print(quote)