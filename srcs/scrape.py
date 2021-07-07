from bs4 import BeautifulSoup
import requests


# Function which find all product information and put them in a dictionary
def get_product_info(soup: BeautifulSoup):
    data = {}
    tr = soup.findAll('tr')
    for header in tr:
        key = header.find('th')
        value = header.find('td')
        data[key.text] = value.text
    return data


# Function which return the UPC serial number
def get_upc(data: dict):
    return data['UPC']


# Function which return the title of the book
def get_title(soup: BeautifulSoup):
    title = soup.find('h1')
    return title.text


# Function which return the price excluding taxes
def get_price_excluding_tva(data: dict):
    return data['Price (excl. tax)']


# Function which return the price including taxes
def get_price_including_tva(data: dict):
    return data['Price (incl. tax)']


# Function which return the number of available books
def get_available(data: dict):
    return data['Availability']


# Function which return the description of product
def get_product_description(soup: BeautifulSoup):
    paragraph = soup.findAll('p', attrs={'class': None})
    for description in paragraph:
        return description.text


# Function which return the category of book
def get_category(soup: BeautifulSoup):
    link = soup.findAll('ul', attrs={'class': 'breadcrumb'})
    for a in link:
        category = a.findAll('a', href=True)
    return category[-1].text


# Function which return the number of reviews
def get_rating(soup: BeautifulSoup):
    rating = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    paragraph = soup.find('div', attrs={'class': 'col-sm-6 product_main'}).findAll('p')
    i = 0
    for p in paragraph:
        if (i == 2):
            return rating[p['class'][1]]
        i += 1


# Function which return the url of image
def get_url_img(soup: BeautifulSoup):
    img = soup.find('div', attrs={'class': 'item active'}).find('img')
    url = img['src'].replace('../..', 'http://books.toscrape.com')
    return url


# Function which return all url of books in a array
def get_url_books(soup: BeautifulSoup):
    array_url = []
    url_site = 'http://books.toscrape.com/catalogue/'
    div = soup.findAll('div', attrs={'class', 'image_container'})
    for link in div:
        a = link.findAll('a')
        for url in a:
            url_book = url['href'].replace('../../../', url_site)
            array_url.append(url_book)
    return array_url


# Function which return all url of all categories in a array
def get_category_books(soup: BeautifulSoup):
    ul = soup.find('ul', attrs={'class': 'nav nav-list'})
    li = ul.findAll('li')
    urls = []
    for link in li:
        a = link.find('a', href=True)
        urls.append(a['href'].replace('catalogue', 'http://books.toscrape.com/catalogue'))
    return urls


# Function which return all name of all categories in a array
def get_all_category_name(soup: BeautifulSoup):
    ul = soup.find('ul', attrs={'class': 'nav nav-list'})
    li = ul.findAll('li')
    names_category = []
    for link in li:
        a = link.find('a', href=True)
        names_category.append(a.text.strip().lower())
    return names_category