import csv
import os
import urllib.request
import re

# Function that creates a csv file and writes header and data in columns
def create_file_csv(filename: str, fields: dict):
    if not os.path.exists('files'):
        os.makedirs('files')
    with open(filename, 'w', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fields[0].keys())
        writer.writeheader()
        for data in fields:
            writer.writerow(data)
    file.close()
    print('Data saved in the following file: ' + filename)

# Function that saves the image of book in a .jpg file
def create_img_book(data: dict):
    if not os.path.exists(f'img/{data[0]["category"]}'):
        os.makedirs(f'img/{data[0]["category"]}')
    for image in data:
        name_book = re.sub("[^0-9a-zA-Z]+", "-", image['title'].lower()) + '.jpg'
        filename = f'img/{image["category"]}/{name_book}'
        urllib.request.urlretrieve(image['image_url'], filename)
        print('Image saved in the following file: ' + filename)