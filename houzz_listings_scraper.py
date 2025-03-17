import requests
from bs4 import BeautifulSoup
import json

def scrape_houzz_search_listings(url):
    products = []

    while url:
        print(f'Scraping {url}')
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            for item in soup.select('div[data-container="Product List"] > div.hz-product-card'):
                title = item.select_one('a.hz-product-card__product-title').text.strip() if item.select_one('a.hz-product-card__product-title') else 'N/A'
                price = item.select_one('span.hz-product-price').text.strip() if item.select_one('span.hz-product-price') else 'N/A'
                rating = item.select_one('span.star-rating')['aria-label'].replace('Average rating: ', '') if item.select_one('span.star-rating') else 'N/A'
                image_url = item.find('img')['src'] if item.find('img') else 'N/A'
                product_link = item.find('a')['href'] if item.find('a') else 'N/A'

                product_data = {
                    'title': title,
                    'price': price,
                    'rating': rating,
                    'image_url': image_url,
                    'product_link': product_link,
                }
                products.append(product_data)

            # Handle pagination
            url = get_next_page_url(soup)

        else:
            print(f'Failed to retrieve the page: {response.status_code}')
            break

    return products

def get_next_page_url(soup):
    next_button = soup.find('a', class_='hz-pagination-link--next')
    return 'https://www.houzz.com' + next_button['href'] if next_button else None

def save_to_json(data, filename='houzz_products.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f'Data saved to {filename} successfully!')

# Main function to run the scraper
if __name__ == '__main__':
    start_url = 'https://www.houzz.com/products/bathroom-vanities-and-sink-consoles/best-sellers--best-sellers'
    listings = scrape_houzz_search_listings(start_url)
    save_to_json(listings)