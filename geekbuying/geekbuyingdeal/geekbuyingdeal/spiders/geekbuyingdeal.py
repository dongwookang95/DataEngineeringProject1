# -*- coding: utf-8 -*-
import scrapy


class GeekbuyingdealSpider(scrapy.Spider):
    name = 'geekbuyingdeal'
    allowed_domains = ['geekbuying.com']
    start_urls = ['https://geekbuying.com/bestselling']

    def parse(self, response):
        products = response.xpath("//div[@class='li_cont']")
        for product in products:
            product_name = product.xpath(".//a[@class='items_p']/text()").get()
            product_url = product.xpath(".//a[@class='items_p']/@href").get()
            product_price = product.xpath(".//span/text()").get()
            yield{
                'name' : product_name,
                'url' : product_url,
                'price' : product_price 
                }
            
        
