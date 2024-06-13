import scrapy
import json

class StockSpider(scrapy.Spider):
    name = 'stock_spider'
    allowed_domains = ['ilboursa.com']

    def start_requests(self):
        with open('companies.json') as f :
            companies = json.load(f)['companies']


    
