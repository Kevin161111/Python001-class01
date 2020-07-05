# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.exceptions import NotConfigured

class DoubanPipeline(object):

    def __init__(self, auto_encoding='utf-8',dbInfo=None):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db= dbInfo['db']

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.get('MYSQL_INFO'):
            raise  NotConfigured
        dbinfo = crawler.settings.get('MYSQL_INFO')
        auto_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING','utf-8')
        return cls(auto_encoding,  dbinfo)    

    def open_spider(self,spider):
        print('db connected')
        self.db = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.db,
            charset = 'utf8'
        )
        self.cursor = self.db.cursor()

    def close_spider(self,spider):
        print('db closed')
        self.db.close()

    def process_item(self, item, spider):

        # print(item['title'])
        # print(item['link'])

        sql ="INSERT INTO `top250` (`id`, `title`,`link`,`content`) VALUES (%s, %s, %s , %s)"
        values = (item['m_id'],item['title'],item['link'],item['content'])
        try:
            self.cursor.execute(sql,values)
            self.db.commit()
            print('----insert db')
        except Exception as e:
            self.db.rollback()
            print(e)
        return item



