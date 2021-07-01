import csv
import os

header = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax',
          'number_available', 'product_description', 'category', 'review_rating', 'image_url']


# Function who creates a csv file and writes header and data in columns
def create_file_csv(directory: str, filename: str, fields: list):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(filename, 'w', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerows([fields])
    file.close()
