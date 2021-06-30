from bs4 import BeautifulSoup


def get_product_info(soup: BeautifulSoup):
    data = {}
    tr = soup.findAll('tr')
    for header in tr:
        key = header.find('th')
        value = header.find('td')
        data[key.text] = value.text
    return data


def get_upc(data: dict):
    return data['UPC']


def get_title(soup: BeautifulSoup):
    title = soup.find('h1')
    return title.text


def get_price_excluding_tva(data: dict):
    return data['Price (excl. tax)']


def get_price_including_tva(data: dict):
    return data['Price (incl. tax)']


def get_available(data: dict):
    return data['Availability']


def get_product_description(soup: BeautifulSoup):
    paragraph = soup.findAll('p', attrs={'class': None})
    for description in paragraph:
        return description.text
