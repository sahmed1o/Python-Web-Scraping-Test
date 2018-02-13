import requests
from bs4 import BeautifulSoup

# link we are using: http://books.toscrape.com/


def get_books(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        get_source = requests.get(url)
        plain_text = get_source.text
        soap_scrape = BeautifulSoup(plain_text, 'html.parser')
        for link in soap_scrape.find_all('img', {'class': 'thumbnail'}):
            href = 'http://books.toscrape.com/' + link.get('src')
            print(href)
        page += 1


get_books(2)

