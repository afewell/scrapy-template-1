import os
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MySpider(CrawlSpider):
    name = 'myspider'

    allowed_domains = [os.getenv('ALLOWED_DOMAINS')]
    start_urls = [os.getenv('START_URLS')]

    rules = (
        Rule(LinkExtractor(allow=os.getenv('ALLOW_RULE')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Define your parsing logic here
        pass
