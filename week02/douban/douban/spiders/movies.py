# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']


    def start_requests(self):
        for i in range(10):
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=False)

    def parse(self, response):
        # print('-'*100)
        # print(response.text)
        # print('-'*100)
        
        movies = Selector(response=response).xpath('//div[@class="hd"]')
        
        for movie in movies:            
            title = movie.xpath('./a/span/text()')
            link = movie.xpath('./a/@href')

            item = DoubanItem()
            item['title'] = title.extract_first().strip()
            item['link'] = link.extract_first().strip()
            # print(item)
            yield scrapy.Request(url=item['link'],meta= {'item':item},callback=self.parse_link,dont_filter=False)

    def parse_link(self, response):
        """ 
        获取对应标题的电影简介
        """
        # 反爬检测
        # print('-'*100)
        # print(response.text)
        # print('-'*100)
        item = response.meta['item'] 
        content = Selector(response=response).xpath('//div[@id="link-report"]/span/text()')
        m_id = Selector(response=response).xpath('//span[@class="top250-no"]/text()').extract_first().strip().split('.')[-1]
        item['content'] = content.extract_first().strip()
        item['m_id'] = m_id
        # print('-'*100)
        # print(item)
        # print('-'*100)
        yield item



