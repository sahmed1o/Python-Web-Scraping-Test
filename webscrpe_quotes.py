import requests
from bs4 import BeautifulSoup

# link we are using: http://quotes.toscrape.com/page/1/


def get_quotes(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://quotes.toscrape.com/page/' + str(page) + '/'
        get_source = requests.get(url)
        plain_text = get_source.text
        soap_scrape = BeautifulSoup(plain_text, 'html.parser')
        for contentstuff in soap_scrape.find_all('span', {'class': 'text'}):
            content = contentstuff.string
            print(content)
            print('\n')
        page += 1


get_quotes(2)

