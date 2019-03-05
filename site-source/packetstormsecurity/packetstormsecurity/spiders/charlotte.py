## Import required python libraries and modules such as ItemLoader and Item Class
import time
import scrapy
from scrapy.loader import ItemLoader
from packetstormsecurity.items import PacketstormsecurityItem

ts = time.gmtime()
timestamp = (time.strftime("%Y-%m-%d %H:%M:%S", ts))
# Ouput example GMT 2019-02-26 15:59:56


## Setup Crawl with allowed_domains and start_urls to be Crawled
class CharlotteSpider(scrapy.Spider):
    name = 'charlotte'
    allowed_domains = ['packetstormsecurity.com']
    start_urls = ['https://packetstormsecurity.com/files/tags/exploit/']

## Define xpath or css selectors for data scrape
## Assign scraped data to Items fields via ItemLoader
## See items.py for declared Items fields for ingestion Pipline
    def parse(self, response):
        all_items = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "file", " " ))]')
        for items in all_items:
            title = items.css('.ico::text').extract()
            refer = items.css('.refer *::text').extract()
            datetime = items.css('.datetime *::text').extract()
            detail = items.css('p::text').extract()
            tags = items.css('.tags *::text').extract()
            cve = items.css('.cve *::text').extract()
            link = items.css('.ico::attr(href)').extract()

## Yield all scraped Items
## Items will be imported into ElasticSearch via Scrapy ElasticSearch
## See settings.py line item ITEM_PIPELINES for ElasticSearch import setting
            item = PacketstormsecurityItem()
            item['title'] = title
            item['refer'] = refer
            item['datetime'] = datetime
            item['detail'] = detail
            item['tags'] = tags
            item['cve'] = cve
            item['link'] = link
            item['timestamp'] = timestamp
            yield item
