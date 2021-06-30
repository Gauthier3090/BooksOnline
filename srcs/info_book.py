import requests
import file
import scrape
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/" \
      "the-rise-and-fall-of-the-third-reich-a-history-of-nazi-germany_454/index.html"

response = requests.get(url)
response.encoding = 'utf-8'

filename = 'files/information.csv'
data = []
dictionary = {}

if __name__ == "__main__":
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        data.append(url)
        dictionary = scrape.get_product_info(soup)
        data.append(scrape.get_upc(dictionary))
        data.append(scrape.get_title(soup))
        data.append(scrape.get_price_excluding_tva(dictionary))
        data.append(scrape.get_price_including_tva(dictionary))
        data.append(scrape.get_available(dictionary))
        data.append(scrape.get_product_description(soup))
        file.create_file_csv(filename, data)
        print("Data saved in the following csv file : " + filename, end="")
    else:
        print("Error: url not found", end="")
