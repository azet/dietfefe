# -*- coding: utf-8 -*-
import scrapy

from dietfefe.items import DietfefeItem

class FefeSpider(scrapy.Spider):
    name = "fefe"
    allowed_domains = ["blog.fefe.de"]
    start_urls = (
        'https://blog.fefe.de/',
    )

    def parse(self, response):
        for link in response.xpath('//ul/li/a/@href'):
            item          = DietfefeItem()
            item['link']  = link.extract()
            if not "?ts" in item['link']: yield item
