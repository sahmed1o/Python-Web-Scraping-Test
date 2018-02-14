import requests
from bs4 import BeautifulSoup

# link we are using: http://books.toscrape.com/


def get_books(all_pages):
    page = 1
    while page <= all_pages:
        get_source = requests.get('http://books.toscrape.com/catalogue/page-' + str(page) + '.html')
        soap_scrape = BeautifulSoup(get_source.text, 'html.parser')
        for link in soap_scrape.find_all('img', {'class': 'thumbnail'}):
            print('http://books.toscrape.com/' + link.get('src'))
        page += 1


get_books(2)

