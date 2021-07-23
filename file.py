import csv
import os
import urllib.request


def create_file_csv(filename: str, fields: dict):
    """ Function that creates a csv file and writes header and data in columns """
    if not os.path.exists('files'):
        os.makedirs('files')
    with open(filename, 'w', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fields[0].keys())
        writer.writeheader()
        for data in fields:
            writer.writerow(data)
    file.close()
    print('Data saved in the following file: ' + filename)


def create_img_book(url: str, category: str, upc: str):
    """ Function that saves the image of book in a .jpg file """
    folderpath = f'img/{category}'
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    name_book = upc + '.jpg'
    filename = f'{folderpath}/{name_book}'
    urllib.request.urlretrieve(url, filename)
    print('Image saved in the following file: ' + filename)
