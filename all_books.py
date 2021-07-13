from requests import get
from os import path
from bs4 import BeautifulSoup
from shutil import rmtree
from file import create_file_csv, create_img_book


# Function check if the string is empty or not
def check_empty(text: str):
    if not text:
        return ''
    return text.text


# Function that retrieves informations of a book from its url
def get_info_book(url: str):
    rating = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return {
        'url' : url,
        'upc': check_empty(soup.select_one('table > tr:nth-child(1) > td')),
        'title': check_empty(soup.select_one('.product_main > h1')),
        'price_including_tax': check_empty(soup.select_one('table > tr:nth-child(4) > td')),
        'price_excluding_tax': check_empty(soup.select_one('table > tr:nth-child(3) > td')),
        'number_available': check_empty(soup.select_one('table > tr:nth-child(6) > td')),
        'product_description': check_empty(soup.select_one('#content_inner > article > p')),
        'category': check_empty(soup.select_one('.breadcrumb > li:nth-child(3) > a')),
        'review_rating': rating[soup.select_one('.product_main > p.star-rating')['class'][1]],
        'image_url': soup.select_one('#product_gallery > div > div > div > img')['src'].replace('../..', 'http://books.toscrape.com')
    }


# Function that returns all urls of books in an array
def get_url_books(soup: BeautifulSoup):
    array_url = []
    url_site = 'http://books.toscrape.com/catalogue/'
    div = soup.findAll('div', attrs={'class', 'image_container'})
    for link in div:
        a = link.findAll('a')
        for url in a:
            url_book = url['href'].replace('../../', url_site)
            array_url.append(url_book)
    return array_url


if __name__ == '__main__':
    if path.exists('files'):
        rmtree('files')
    if path.exists('img'):
        rmtree('img')
    for i in range(1, 51):
        url = 'https://books.toscrape.com/catalogue/category/books_1/page-' + str(i) + '.html'
        response = get(url)
        if response.ok:
            print(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            url_books = get_url_books(soup)
            for book in url_books:
                data = get_info_book(book)
                csv = 'files/' + data['category'] + '.csv'
                create_file_csv('files', csv, data)
                create_img_book(data['image_url'], data['title'])
        else:
            print('Error: url not found !')