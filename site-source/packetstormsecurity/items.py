import scrapy

class PacketstormsecurityItem(scrapy.Item):
    title = scrapy.Field()
    refer = scrapy.Field()
    datetime = scrapy.Field()
    detail = scrapy.Field()
    tags = scrapy.Field()
    cve = scrapy.Field()
    link = scrapy.Field()
    timestamp = scrapy.Field()
