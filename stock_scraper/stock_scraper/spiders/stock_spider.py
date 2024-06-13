import scrapy
import json
import sys
sys.path.append('C:/Users/Kahla/OneDrive/Documents/Tunisia_Stock_Market/stock_scraper/stock_scraper')

from update_dates import update_json_file

class StockSpider(scrapy.Spider):
    name = 'stock_spider'
    allowed_domains = ['ilboursa.com']

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

        # Save data to JSON file
        file_name = f"{symbol}.json"
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        # Call update_json_file function to update the saved JSON file
        update_json_file(file_name)