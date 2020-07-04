# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DoubanPipeline(object):

    def process_item(self, item, spider):
        print('*'*100)
        print(int(item['m_id']))
        print(item['title'])
        print(item['link'])
        print(item['content'])


        return item


# class DoubanPipeline(object):

#     dbInfo = {
#     'host': 'localhost',
#     'port': 3306,
#     'user': 'root',
#     'password': 'gold2020',
#     'db':'doubanmovies'
# }

#     def __init__(self, dbInfo):
#         self.host = dbInfo['host']
#         self.port = dbInfo['port']
#         self.user = dbInfo['user']
#         self.password = dbInfo['password']
#         self.db= dbInfo['db']

#     def open_spider(self,spider):
#         print('连接数据库')
#         self.db = pymysql.connect(
#             host = self.host,
#             port = self.port,
#             user = self.user,
#             password = self.password,
#             database = self.db,
#             charset = 'utf-8'
#         )
#         self.cursor = self.db.cursor()

#     def close_spider(self,spider):
#         print('关闭数据库')
#         self.db.close()

#     def process_item(self, item, spider):
      
#         print(item['m_d'])
#         print(item['title'])
#         print(item['link'])
#         print(item['content'])


#         sql ="INSERT INTO `top250` (`id`, `title`,`link`,`content`) VALUES (%d, %s, %s , %s)"
#         values = (int(item['m_d']),item['title'],item['link'],item['content'])

#         self.cursor.execute(sql,values)
#         print('----insert db')
#         self.db.commit()
#         return item



# #----------------------------------------------------------------
# import pymysql.cursors

# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='gold2020',
#                              db='test',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)

# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `tb1` (`id`, `name`) VALUES (%s, %s)"
#         # 执行批量插入
#         values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
#         cursor.executemany(sql, values)
#         # cursor.execute(sql, ('2', 'jery'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `name` FROM `tb1` WHERE `id`=%s"
#         cursor.execute(sql, ('2',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()





# import pymysql

# conn = pymysql.connect(host = 'localhost',
#                        port = 3306,
#                        user = 'root',
#                        password = 'gold2020',
#                        database = 'test',
#                        charset = 'utf8mb4'
#                         )

# # 获得cursor游标对象
# con1 = conn.cursor()

# # 操作的行数
# count = con1.execute('select * from tb1;')
# print(f'查询到 {count} 条记录')


# # 获得一条查询结果
# result = con1.fetchone()
# print(result)

# # 获得所有查询结果
# print(con1.fetchall())

# con1.close()
# conn.close()



# # 开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束
# import pymysql

# dbInfo = {
#     'host' : 'localhost',
#     'port' : 3306,
#     'user' : 'root',
#     'password' : 'gold2020',
#     'db' : 'test1'
# }

# sqls = ['select 1', 'select VERSION()']

# result = []

# class ConnDB(object):
#     def __init__(self, dbInfo, sqls):
#         self.host = dbInfo['host']
#         self.port = dbInfo['port']
#         self.user = dbInfo['user']
#         self.password = dbInfo['password']
#         self.db = dbInfo['db']
#         self.sqls = sqls

#         # self.run()

#     def run(self):
#         conn = pymysql.connect(
#             host = self.host,
#             port = self.port,
#             user = self.user,
#             password = self.password,
#             db = self.db
#         )
#         # 游标建立的时候就开启了一个隐形的事物
#         cur = conn.cursor()
#         try:
#             for command in self.sqls:
#                 cur.execute(command)
#                 result.append(cur.fetchone())
#             # 关闭游标
#             cur.close()
#             conn.commit()
#         except:
#             conn.rollback()
#         # 关闭数据库连接
#         conn.close()

# if __name__ == "__main__":
#     db = ConnDB(dbInfo, sqls)
#     db.run()
#     print(result)
