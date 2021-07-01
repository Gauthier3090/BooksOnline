import requests
from bs4 import BeautifulSoup


def get_url_books(soup: BeautifulSoup):
    array_url = []
    div = soup.findAll('div', attrs={'class', 'image_container'})
    for link in div:
        a = link.findAll('a')
        for url in a:
            url_book = url['href'].replace('../../../', 'http://books.toscrape.com/catalogue/')
            array_url.append(url_book)
    return array_url


if __name__ == '__main__':
    url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
    url_books = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        url_books = get_url_books(soup)
        for element in url_books:
            print(element)
    else:
        print('Url not found', end='')
