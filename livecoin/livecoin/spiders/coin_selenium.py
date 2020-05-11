# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.chrome.options import Options
from shutil import which

class CoinSpider(scrapy.Spider):
    name = 'coin_selenium'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ["https://www.livecoin.net/en"]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("./chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920,1000)
        driver.get("https://www.livecoin.net/en")

        ltc_tab = driver.find_element_by_class_name("filterPanelItem___2z5Gb")
        ltc_tab[5].click()
        
        self.html = driver.page_source
        driver.close()


    def parse(self, response):
        resp = Selector(test=self.html)

        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield{
                'currency pair' : currency.xpath("//div[1]/div/text()"),
                'volume(24h)' : currency.xpath("//div[2]/span/text()")
            }
       
        