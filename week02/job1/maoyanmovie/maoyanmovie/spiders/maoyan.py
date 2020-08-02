# -*- coding: utf-8 -*-
import scrapy
import traceback
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        try:
            yield scrapy.Request(url=url, callback=self.parse)
        except Exception as e:
            print(traceback.format_exc())

    def parse(self, response):
        # 打印网页url
        # print(response.url)
        # 打印网页内容
        # print(response.text)

        dd_nodes = Selector(response=response).xpath(
            '//*[@id="app"]/div/div[2]/div[2]/dl[@class="movie-list"]//dd')[:10]
        for dd_node in dd_nodes:
            item = MaoyanmovieItem()
            title = dd_node.xpath(
                './div[1]/div[2]/a/div/div[1]/span[1]/text()')
            film_type = dd_node.xpath('./div[1]/div[2]/a/div/div[2]/text()')
            film_date = dd_node.xpath('./div[1]/div[2]/a/div/div[4]/text()')
            item['title'] = ''.join(title.extract()).strip()
            item['film_type'] = ''.join(film_type.extract()).strip()
            item['film_date'] = ''.join(film_date.extract()).strip()
            yield item
