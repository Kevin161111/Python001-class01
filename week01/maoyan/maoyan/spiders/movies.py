# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem
from http.cookies import SimpleCookie

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    # 处理反爬的问题 添加 cookies
    cookies_fromchrome = '__mta=208417709.1592895912492.1592902918645.1592903952867.7; uuid_n_v=v1; uuid=DF9CCBB0B51F11EA801551553EAD9849A9C6A4B3E2894835A13DFBE0903318F2; _csrf=b440c76ad9bd8b530488f522785e6cf7af43ac1e907b9196a84bc71857d4234e; _lxsdk_cuid=172dffeb93ec8-0d64910ea0f05a-143e6257-1fa400-172dffeb93ec8; mojo-uuid=6a2c8527c33ed9dd8462351a67bb364e; mojo-session-id={"id":"5fa649bfa4a5fb40547b9af2b7ae5a30","time":1592898021553}; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172e0281287bdf-06e09e70bab7de-2076244f-546797-172e0281288c3f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172e0281287bdf-06e09e70bab7de-2076244f-546797-172e0281288c3f%22%7D; _lxsdk=DF9CCBB0B51F11EA801551553EAD9849A9C6A4B3E2894835A13DFBE0903318F2; lt=sbcAoSSv2aNOkmQO1M30XtzxY4oAAAAA5woAAM42swSU-Amm1PnUAOMGoyjjYbuzAnq3nio6jK_ArkGALUH-whiVT6KsP7yiYWj32g; lt.sig=ytlNcmJAcMmZ5ZqM84NQiRBdoqM; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592906608,1592906937,1592906948,1592906968; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592906968; __mta=208417709.1592895912492.1592903952867.1592906969162.8; mojo-trace-id=50; _lxsdk_s=172e01ee84e-47c-6be-c2b%7C%7C99'

    cookie = SimpleCookie(cookies_fromchrome)
    cookies = {i.key:i.value for i in cookie.values()}

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象
    # star_requests()方法读取 start_urls列表中的url并生成 request对象，发送给 引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):

        yield scrapy.Request(url=self.start_urls[0],callback=self.parse,dont_filter=False,cookies=self.cookies)

    # 解析函数
    def parse(self, response):
        """  
        获取电影的标题和链接
        """
        # 打印网页的url
        print(response.url)
        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies: 
            item = MaoyanItem()
            title = movie.xpath('./a/text()') # 电影名称
            link =  movie.xpath('./a/@href') # 链接
            item['title'] = title.extract_first().strip()
            item['link'] = 'https://' + self.allowed_domains[0] + link.extract_first().strip() # 拼接完整的 url
            yield scrapy.Request(url=item['link'],meta={'item': item},callback=self.parse2)

    def parse2(self,response):
        """  
        到对应标题的链接中获取电影信息
        """
        item = response.meta['item']
        infos = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        print(infos)
        for info in infos:
            category = info.xpath('./ul/li/a/text()').extract()
            date = info.xpath('./ul/li[last()]/text()').extract_first().strip()
            item['category'] = category
            item['date'] = date

        yield item
        
         

   