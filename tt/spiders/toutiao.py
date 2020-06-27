# -*- coding: utf-8 -*-
import urllib.request

import scrapy
from scrapy import Request

from tt.items import TtItem
from lxml import etree

class ToutiaoSpider(scrapy.Spider):
    name = "sohu"
    allowed_domains = ["sohu.com"]
    start_urls = (
        'http://www.sohu.com/',
    )

    def sec(self, url):
        sec_html = urllib.request.urlopen(url)
        sec_response = sec_html.read().decode('utf-8')
        etree_sec_response = etree.HTML(sec_response)
        # content = etree_sec_response.xpath('article[@class="article"]/p/text()')
        # print(content)
        print(sec_response[
              sec_response.find('<article') + 1 : sec_response.rfind('</article>')])
        print('-----------------------------------')

    def parse(self, response):
        news = response.xpath('//div[@class="news"]/p/a')
        for new in news:
            item = TtItem()
            item['title'] = new.xpath('./@title').extract()[0]
            item['href'] = new.xpath('./@href').extract()[0]
            print('+++++++++++++++++++++++++++++++++++++++++')
            yield item
            if item['href']:
                yield Request(item['href'], callback=self.sec(item['href']))
