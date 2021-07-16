from bs4 import BeautifulSoup
import requests
import file

# Function that checks if the string is empty or not
def check_empty(text: str):
    if not text:
        return ''
    return text.text

# Function that converts a string to an integer
def str_to_int(text: str):
    num = ""
    for letter in text:
        if letter.isdigit():
            num += letter
    return num

# Function that retrieves informations of a book from its url
def get_info_book(url: str):
    rating = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return {
        'url' : url,
        'upc': check_empty(soup.select_one('table > tr:nth-child(1) > td')),
        'title': check_empty(soup.select_one('.product_main > h1')),
        'price_including_tax': check_empty(soup.select_one('table > tr:nth-child(4) > td')),
        'price_excluding_tax': check_empty(soup.select_one('table > tr:nth-child(3) > td')),
        'number_available': str_to_int(check_empty(soup.select_one('table > tr:nth-child(6) > td'))),
        'product_description': check_empty(soup.select_one('#content_inner > article > p')),
        'category': check_empty(soup.select_one('.breadcrumb > li:nth-child(3) > a')),
        'review_rating': rating[soup.select_one('.product_main > p.star-rating')['class'][1]],
        'image_url': soup.select_one('#product_gallery > div > div > div > img')['src'].replace('../..', 'http://books.toscrape.com')
    }

# Function that returns the list of book urls page by page
def get_next_book():
    for i in range(1, 51):
        print(f'https://books.toscrape.com/catalogue/category/books_1/page-{i}.html')
        response = requests.get(f'https://books.toscrape.com/catalogue/category/books_1/page-{i}.html')
        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')
            for url in [a['href'].replace('../../', 'http://books.toscrape.com/catalogue/') for a in soup.select('article > h3 > a')]:
                yield url

if __name__ == '__main__':
    data = {}
    for book_url in get_next_book():
        book = get_info_book(book_url)
        if not book['category'] in data:
            data.setdefault(book['category'], [])
        data[book['category']].append(book)
    for category in data.keys():
        file.create_file_csv(f'files/{category}.csv', data[category])
        file.create_img_book(data[category])