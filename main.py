import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce website you want to scrape
url = 'https://www.jumia.co.ke/mlp-pay-day/'

# Send a request to the URL
response = requests.get(url);

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Create a CSV file to save the extracted data
csv_file = open('products.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image', 'Name', 'Rating', 'Price'])

# Extract product information from the HTML content
products = soup.find_all('a', class_='core')

for product in products:
    # Extract image URL
    image = product.find('img')['data-src']

    # Extract product name
    name = product.find('h3',class_='name').text.strip()

    # Extract brand name
    # brand = product.find('div', class_='-pvxs').text.strip()

    # Extract product rating
    rating = product.find('div', class_='stars').text.strip()

    # Extract product price
    price = product.find('div', class_='prc').text.strip()

    # Extract product description
    # description = product.find('p').text.strip()

    # Write product information to the CSV file
    csv_writer.writerow([image, name, rating, price])

# Close the CSV file
csv_file.close()
