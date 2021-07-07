import requests
import scrape
import file
import info_book
from bs4 import BeautifulSoup

def get_books_category(url: str, filename: str):
    next_page = True
    i = 0
    j = 1
    while (next_page):
        if i == 1:
            url = url.replace('index', 'page-' + str(j))
        if i >= 2:
            url = url.replace('page-' + str(i), 'page-' + str(j))
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')
            url_books = scrape.get_url_books(soup)
            index = 0
            for element in url_books:
                if response.ok:
                    data = info_book.get_info_book(element)
                    if (index == 0 and i == 0):
                        file.create_file_csv('files', filename, data)
                    else:
                        file.append_file_csv(filename, data)
                    index += 1
            i += 1
            j += 1
        else:
            next_page = False

if __name__ == '__main__':
    url = 'https://books.toscrape.com/catalogue/category/books/default_15/index.html'
    filename = "files/category.csv"
    get_books_category(url, filename)
    print("Data saved in the following csv file : " + filename)
