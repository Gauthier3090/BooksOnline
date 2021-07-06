import requests
import scrape
import file
import category
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://books.toscrape.com/index.html'
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        url_category = scrape.get_category_books(soup)
        names_category = scrape.get_all_category_name(soup)
        for name, link in zip(names_category[1:], url_category[1:]):
            filename = 'files/' + name + '.csv'
            category.get_books_category(link, filename)
            print("Data saved in the following csv file : ", end="")
            print(filename)