import scrapy
import json
from scrapy import signals
from scrapy.signalmanager import dispatcher

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.update_dates import update_json_file
from utils.join_data import join_json_data_to_csv

class StockSpider(scrapy.Spider):
    name = 'stock_spider'
    allowed_domains = ['ilboursa.com']

    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def start_requests(self):
        with open('companies.json') as f:
            companies = json.load(f)['companies']

        for company in companies:
            symbol = company['ticker_symbol']
            url = f"https://www.ilboursa.com/api/charting/GetTicksEOD?symbol={symbol}&length=3650&period=0&guid=OqHyDClA4XCDw4J3AQUrTJEIK1haIBNtf29AbzHll5M"
            yield scrapy.Request(url, self.parse, meta={'symbol': symbol})

    def parse(self, response):
        symbol = response.meta['symbol']
        data = json.loads(response.body)

        file_name = f"companies_data/{symbol}.json"
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        update_json_file(file_name)

    def spider_closed(self, spider):
        join_json_data_to_csv('companies_data', 'companies_data/output.csv')
