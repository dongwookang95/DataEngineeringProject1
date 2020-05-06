# -*- coding: utf-8 -*-
import scrapy


class GeekbuyingdealSpider(scrapy.Spider):
    name = 'geekbuyingdeal'
    allowed_domains = ['geekbuying.com']
    def start_requests(self):
        yield scrapy.Request(url='https://geekbuying.com/bestselling', callback=self.parse, header={
        'Mozilla/5.0 (Macinto sh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
        })
    def parse(self, response):
        products = response.xpath("//div[@class='li_cont']")
        for product in products:
            product_name = product.xpath(".//a[@class='items_p']/text()").get()
            product_url = product.xpath(".//a[@class='items_p']/@href").get()
            product_price = product.xpath(".//span/text()").get(),
            

            yield{
                'name' : product_name,
                'url' : product_url,
                'price' : product_price,
                'User-Agent' : response.request.headers['User-Agent'].decode('utf-8')
                }
        #next_page = response.xpath().get()       
        #if next_page:
        #   yield response.follow(url=next_page, callback=self.parse, header={
        # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'})

    #Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36
        
