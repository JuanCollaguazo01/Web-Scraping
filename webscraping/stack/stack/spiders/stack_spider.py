import scrapy
from scrapy import Spider
from scrapy import Selector

from stack.items import StackItem


class StackSpider(scrapy.Spider):
    name = 'stack'
    allowed_domains = ['stackoverflow.com']
    start_urls = [
    'http://stackoverflow.com/questions?pagesize=50&sort=newest'
    ]

    def parse(self, response):
        questions=Selector(response).xpath('//div[@class="summary"]')

        for question in questions:
        	item=StackItem()
        	item['title']=question.xpath('h3/a[@class="question-hyperlink"]/text()').extract()[0]
        	item['url']=question.xpath('h3/a[@class="question-hyperlink"]/@href').extract()[0]
        	yield item
