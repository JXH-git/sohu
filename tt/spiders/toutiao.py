# -*- coding: utf-8 -*-
import scrapy

from tt.items import TtItem


class ToutiaoSpider(scrapy.Spider):
    name = "sohu"
    allowed_domains = ["sohu.com"]
    start_urls = (
        'http://www.sohu.com/',
    )

    def parse(self, response):
        news = response.xpath('//div[@class="news"]/p/a')
        for new in news:
            item = TtItem()
            item['title'] = new.xpath('./@title').extract()[0]
            item['href'] = new.xpath('./@href').extract()[0]
            print('+++++++++++++++++++++++++++++++++++++++++')
            yield item
