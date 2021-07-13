from csv import DictWriter
from os import makedirs, stat, path
from urllib import request
from re import sub

# Function that creates a csv file and writes header and data in columns
def create_file_csv(directory: str, filename: str, fields: list):
    if not path.exists('files'):
        makedirs('files')
    with open(filename, 'a', encoding='utf-8-sig') as file:
        writer = DictWriter(file, fields.keys())
        if stat(filename).st_size == 0:
            writer.writeheader()
        writer.writerow(fields)
    file.close()
    print('Data saved in the following file: ' + filename)

# Function that saves the image of book in a .jpg file
def create_img_book(url: str, name_book: str):
    if not path.exists('img'):
        makedirs('img')
    name_book = sub("[^0-9a-zA-Z]+", "-", name_book.lower())
    filename = 'img/' + name_book + '.jpg'
    request.urlretrieve(url, filename)
    print('Image saved in the following file: ' + filename)