import scrapy
from scrapy.loader import ItemLoader
from packetstormsecurity.items import PacketstormsecurityItem


class CharlotteSpider(scrapy.Spider):
    name = 'charlotte'
    allowed_domains = ['packetstormsecurity.com']
    start_urls = ['https://packetstormsecurity.com/files/tags/exploit/']


    def parse(self, response):
        all_items = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "file", " " ))]')
        for item in all_items:
            title = item.css('.ico::text').extract()
            refer = item.css('.refer *::text').extract()
            datetime = item.css('.datetime *::text').extract()
            detail = item.css('p::text').extract()
            tags = item.css('.tags *::text').extract()
            cve = item.css('.cve *::text').extract()
            link = item.css('.ico::attr(href)').extract()
            yield {
                'title' : title,
                'refer' : refer,
                'datetime' : datetime,
                'detail' : detail,
                'tags' : tags,
                'cve' : cve,
                'link' : link
            }
