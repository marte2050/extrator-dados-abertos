import scrapy


class VagasItem(scrapy.Item):
    files = scrapy.Field()
    file_urls = scrapy.Field()
