# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockScraperItem(scrapy.Item):
    date = scrapy.Field()
    current_price = scrapy.Field()
    volume = scrapy.Field()
    opening_price = scrapy.Field()
    closing_price = scrapy.Field()
    highest_price = scrapy.Field()
    lowest_price = scrapy.Field()
    variation = scrapy.Field()
    volatility = scrapy.Field()
    capital_exchange = scrapy.Field()
    market_capitalization = scrapy.Field()
    isin = scrapy.Field()
    ticker_symbol = scrapy.Field()
    pass
