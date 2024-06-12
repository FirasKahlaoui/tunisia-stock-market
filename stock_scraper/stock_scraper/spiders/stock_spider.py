import scrapy
from stock_scraper.items import StockScraperItem
import json

# Load the JSON file
file_path = 'companies.json'
with open(file_path, 'r') as file:
    data = json.load(file)
