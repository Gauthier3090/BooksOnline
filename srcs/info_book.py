import requests
import file
import scrape
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/" \
          "the-rise-and-fall-of-the-third-reich-a-history-of-nazi-germany_454/index.html"
    filename = 'files/information.csv'
    data = []
    dictionary = {}
    response = requests.get(url)
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
        data.append(scrape.get_category(soup))
        data.append(scrape.get_rating(dictionary))
        data.append(scrape.get_url_img(soup))
        file.create_file_csv(filename, data)
        print("Data saved in the following csv file : " + filename, end="")
    else:
        print("Error: url not found", end="")
