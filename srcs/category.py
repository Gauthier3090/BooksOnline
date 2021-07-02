import requests
import scrape
import file
from bs4 import BeautifulSoup


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


if __name__ == '__main__':
    i = 1
    url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/'\
        'page-1.html'
    url_books = []
    filename = "files/category.csv"
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        url_books = get_url_books(soup)
        index = 0
        for element in url_books:
            if response.ok:
                data = []
                dictionary = {}
                response = requests.get(element)
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
                if (index == 0):
                    file.create_file_csv('files', filename, data)
                else:
                    file.append_file_csv(filename, data)
                index += 1
        print("Data saved in the following csv file : " + filename, end="")
    else:
        print('Error: Url not found', end='')
