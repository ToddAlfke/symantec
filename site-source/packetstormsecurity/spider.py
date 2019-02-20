import scrapy
from scrapy.loader import ItemLoader
from packetstormsecurity.items import PacketstormsecurityItem


class SpiderSpider(scrapy.Spider):
name = 'spider'
allowed_domains = ['packetstormsecurity.com']
start_urls = ['https://packetstormsecurity.com/files/tags/exploit/']

def parse(self, response):
l = ItemLoader(item=PacketstormsecurityItem(), response=response)
l.add_css('element', 'dl *::text')
return l.load_item()
