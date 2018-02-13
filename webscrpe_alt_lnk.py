import requests
from bs4 import BeautifulSoup

# link we are using: http://books.toscrape.com/
#web scraping

def get_books(all_pages):
    page = 1
    while page <= all_pages:
        url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        get_source = requests.get(url)
        plain_text = get_source.text
        soap_scrape = BeautifulSoup(plain_text, 'html.parser')
        for link in soap_scrape.find_all('article', {'class': 'product_pod'}):
            child_link = link.findChild("h3").findChild("a")
            href = 'http://books.toscrape.com/catalogue/' + child_link.get('href')
            print(href)
            get_single_page(href)
        page += 1


def get_single_page(book_url):
    get_source = requests.get(book_url)
    plain_text = get_source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for book_name in soup.find_all('h1'):
        print("\n")
        print(book_name.string)
    for links in soup.find_all('a'):
        href = 'http://books.toscrape.com/catalogue/' + links.get('href')
        print(href)

get_books(2)

