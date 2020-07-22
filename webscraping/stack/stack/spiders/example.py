import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.epn.edu.ec']
    start_urls = ['http://www.epn.edu.ec/']

    def parse(self, response):
        pass
