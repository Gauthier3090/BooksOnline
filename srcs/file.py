import csv

header = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax',
          'number_available', 'product_description', 'category', 'review_rating', 'image_url']


def create_file_csv(filename: str, fields: list):
    with open(filename, 'w', encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(header)
        writer.writerows([fields])
    file.close()
