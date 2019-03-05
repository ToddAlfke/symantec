import scrapy

class NetsparkerItem(scrapy.Item):
    ns_id = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    timestamp = scrapy.Field()
