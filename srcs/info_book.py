import requests
from requests.api import request
import file
import scrape
from bs4 import BeautifulSoup

def get_info_book(url: str):
    data = []
    dictionary = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data.append(url)
    dictionary = scrape.get_product_info(soup)
    data.append(scrape.get_upc(dictionary))
    data.append(scrape.get_title(soup))
    data.append(scrape.get_price_excluding_tva(dictionary))
    data.append(scrape.get_price_including_tva(dictionary))
    data.append(scrape.get_available(dictionary))
    data.append(scrape.get_product_description(soup))
    data.append(scrape.get_category(soup))
    data.append(scrape.get_rating(dictionary))
    data.append(scrape.get_url_img(soup))
    return data

if __name__ == "__main__":
    url = "https://books.toscrape.com/catalogue/the-grownup_546/index.html"

    filename = 'files/product.csv'
    response = requests.get(url)
    if response.ok:
        data = get_info_book(url)
        file.create_file_csv('files', filename, data)
        print("Data saved in the following csv file : " + filename, end="")
    else:
        print("Error: url not found", end="")
