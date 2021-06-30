from bs4 import BeautifulSoup


# Function who find all product information and put them in a dictionary
def get_product_info(soup: BeautifulSoup):
    data = {}
    tr = soup.findAll('tr')
    for header in tr:
        key = header.find('th')
        value = header.find('td')
        data[key.text] = value.text
    return data


# Function who return the UPC serial number
def get_upc(data: dict):
    return data['UPC']


# Function who return the title of the book
def get_title(soup: BeautifulSoup):
    title = soup.find('h1')
    return title.text


# Function who return the price excluding taxes
def get_price_excluding_tva(data: dict):
    return data['Price (excl. tax)']


# Function who return the price including taxes
def get_price_including_tva(data: dict):
    return data['Price (incl. tax)']


# Function who return the number of available books
def get_available(data: dict):
    return data['Availability']


# Function who return the description of product
def get_product_description(soup: BeautifulSoup):
    paragraph = soup.findAll('p', attrs={'class': None})
    for description in paragraph:
        return description.text
