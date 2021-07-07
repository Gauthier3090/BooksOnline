import csv
import os
import urllib.request
import re

header = ['product_page_url', 'universal_product_code (upc)', 'title',
          'price_including_tax', 'price_excluding_tax',
          'number_available', 'product_description', 'category',
          'review_rating', 'image_url']


# Function which creates a csv file and writes header and data in columns
def create_file_csv(directory: str, filename: str, fields: list):
    if not os.path.exists(directory):
        os.makedirs(directory)
    if os.path.isfile(filename):
        os.remove(filename)
    with open(filename, 'w', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerows([fields])
    file.close()


# Function which appends elements in a csv file without erase
def append_file_csv(filename: str, fields: list):
    with open(filename, 'a', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows([fields])
    file.close()


# Function which saves the image of book in a .jpg file
def create_img_book(url: str, name_book: str):
    if not os.path.exists('img'):
        os.makedirs('img')
    name_book = re.sub("[^0-9a-zA-Z]+", "-", name_book.lower())
    filename = 'img/' + name_book + '.jpg'
    urllib.request.urlretrieve(url, filename)
    print('Image saved in the following file: ' + filename)