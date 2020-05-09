# -*- coding: utf-8 -*-
import scrapy


class Coin2Spider(scrapy.Spider):
    name = 'coin2'
    allowed_domains = ['www.livecoin.net/en']

script = '''
function main(splash, args)
  splash.private_mode_enabled = true
  url = args.url
  assert(splash:go(url))
  assert(splash:wait(1))
  ltc = assert(splash:select_all(".filterPanelItem___2z5Gb"))
  ltc[5]:mouse_click()
  assert(splash:wait(1))
  splash:set_viewport_full()
  return splash:html()
end
'''

def start_requests(self):
    yield SplashRequest(url="https://www.livecoin.net/en", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
    })

    def parse(self, response):
        pass
