import requests
from bs4 import BeautifulSoup

# link we are using: http://quotes.toscrape.com/page/1/


def get_quotes(all_pages):
    page = 1
    while page <= all_pages:
        get_source = requests.get('http://quotes.toscrape.com/page/' + str(page) + '/')
        soap_scrape = BeautifulSoup(get_source.text, 'html.parser')
        for contentstuff in soap_scrape.find_all('span', {'class': 'text'}):
            print(contentstuff.string)
            print('\n')
        page += 1


get_quotes(2)

