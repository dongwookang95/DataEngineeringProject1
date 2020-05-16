# -*- coding: utf-8 -*-
import scrapy


class OpenlibraryLoginSpider(scrapy.Spider):
    name = 'openlibrary_login'
    allowed_domains = ['https://openlibrary.org/account/login']
    start_urls = ['http://https://openlibrary.org/account/login/']

    def parse(self, response):
        pass
