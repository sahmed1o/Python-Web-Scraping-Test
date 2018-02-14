import requests
from bs4 import BeautifulSoup

# link we are using: http://books.toscrape.com/
#web scraping

def get_books(all_pages):
    page = 1
    while page <= all_pages:
        url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        get_source = requests.get(url)
        soap_scrape = BeautifulSoup(get_source.text, 'html.parser')
        for link in soap_scrape.find_all('article', {'class': 'product_pod'}):
            child_link = link.findChild("h3").findChild("a")
            print('http://books.toscrape.com/catalogue/' + child_link.get('href'))
            get_book_info('http://books.toscrape.com/catalogue/' + child_link.get('href'))
        page += 1


def get_book_info(book_url):
    get_source = requests.get(book_url)
    soup = BeautifulSoup(get_source.text, 'html.parser')
    for book_name in soup.find_all('h1'):
        print("\n")
        print(book_name.string)
    for links in soup.find_all('a'):
        print('http://books.toscrape.com/catalogue/' + links.get('href'))

get_books(2)

