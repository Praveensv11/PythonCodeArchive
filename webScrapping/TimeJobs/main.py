from bs4 import BeautifulSoup
import requests
import time
import os 

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):        
        published_date = job.find('span', class_='sim-posted').text.strip()
        if 'few' in published_date:
            company = job.find('h3', class_='joblist-comp-name').text.strip()
            skill = job.find('span', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']

            os.makedirs('posts', exist_ok=True)

            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"company : {company}\n")
                f.write(f"skill : {skill}\n")
                f.write(f"Published_date : {published_date}\n")
                f.write(f"Info : {more_info}\n")


if __name__ == "__main__":
    find_jobs()
