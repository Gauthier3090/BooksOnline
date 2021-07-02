import csv
import os

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


# Function which append elements in a csv file without erase
def append_file_csv(filename: str, fields: list):
    with open(filename, 'a', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows([fields])
    file.close()
