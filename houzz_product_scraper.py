import requests
from bs4 import BeautifulSoup
import json

def scrape_houzz_product_page(url):
    response = requests.get(url)
    product_data = {}

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.select_one('span.view-product-title').text.strip() if soup.select_one('span.view-product-title') else 'N/A'
        price = soup.select_one('span.pricing-info__price').text.strip() if soup.select_one('span.pricing-info__price') else 'N/A'
        description = soup.select_one('div.vp-redesign-description').text.strip() if soup.select_one('div.vp-redesign-description') else 'N/A'
        image_urls = [img['src'] for img in soup.select('div.alt-images__thumb > img')] if soup.select('div.alt-images__thumb > img') else 'N/A'

        product_data = {
            'title': title,
            'price': price,
            'description': description,
            'image_urls': image_urls,
            'product_link': url
        }
    else:
        print(f'Failed to retrieve the product page: {response.status_code}')

    return product_data

def save_product_to_json(product_data, filename='houzz_product.json'):
    with open(filename, 'w') as json_file:
        json.dump(product_data, json_file, indent=4)
    print(f'Product data saved to {filename} successfully!')

# Main function to run the product page scraper
if __name__ == '__main__':
    product_url = 'https://www.houzz.com/product/204153376'
    product_details = scrape_houzz_product_page(product_url)
    save_product_to_json(product_details)