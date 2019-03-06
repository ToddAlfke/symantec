## Import required python libraries and modules such as ItemLoader and Item Class
import time
import scrapy
from scrapy.loader import ItemLoader
from netsparker.items import NetsparkerItem

ts = time.gmtime()
timestamp = (time.strftime("%Y-%m-%d %H:%M:%S", ts))
# Ouput example GMT 2019-02-26 15:59:56

## Setup Crawl with allowed_domains and start_urls to be Crawled
class CharlotteSpider(scrapy.Spider):
    name = 'charlotte'
    allowed_domains = ['netsparker.com']
    start_urls = ['https://www.netsparker.com/web-applications-advisories/']

## Define xpath or css selectors for data scrape
## Assign scraped data to Items fields via ItemLoader
## See items.py for declared Items fields for ingestion Pipline
    def parse(self, response):
        all_items = response.css('tr')
        for items in all_items:
            ns_id = items.css('td::text').extract()
            name = items.css('td > a::text').extract()
            link = items.css('td > a::attr(href)').extract()

## Yield all scraped Items
## Items will be imported into ElasticSearch via Scrapy ElasticSearch
## See settings.py line item ITEM_PIPELINES for ElasticSearch import setting
            item = NetsparkerItem()
            item['ns_id'] = ns_id
            item['name'] = name
            item['link'] = link
            item['timestamp'] = timestamp
            yield item
