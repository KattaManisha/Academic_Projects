import json
import requests
from bs4 import BeautifulSoup

def get_product_price_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    data_components_str = soup.select_one('.cardRoot[data-components]')['data-components']
    data_components = json.loads(data_components_str)
    product_price = data_components['1']['price']['displayString']
    return url, product_price

def get_product_price_ebay(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    x_price_primary_div = soup.find('div', class_='x-price-primary')
    product_price = x_price_primary_div.find('span', class_='ux-textspans').text.strip()
    return url, product_price


