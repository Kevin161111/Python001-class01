# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd 

class MaoyanPipeline(object):
    # 每个 item 管道组件都会调用该方法，并且必须返回一个item对象实例否则 raise DropItem 异常 
    def process_item(self, item, spider):
        title = item['title']
        category = item['category']
        date = item['date']
        movie_info = [[title, category, date]]
        df = pd.DataFrame(movie_info, columns=['title', 'category', 'date'])
        df.to_csv('./movies_1.csv',mode='a',encoding='utf8',index=False,header=False)

        return item 
  
