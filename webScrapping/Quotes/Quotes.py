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
        quotes_datas = soup.find_all('div', class_='quote')
        for quotes_data in quotes_datas:
            quotes_tags = quotes_data.find('div', class_='tags')
            content = quotes_tags.find('meta', class_='keywords')['content']
            
            if user_tags in content:
                quotes_text = quotes_data.find('span', class_='text').text
                print(quotes_text)
        break