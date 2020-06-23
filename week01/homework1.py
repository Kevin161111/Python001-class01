"""  
使用 requests 爬取 猫眼电影 
前10个电影
* 名称
* 电影类型
* 上映时间
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

url = 'https://maoyan.com' # 用于后面 link 拼接
myurl = 'https://maoyan.com/films?showType=3' # 爬取页面
# headers 加入 cookies 否则容易限制ip反扒
header = {
    'Cookie':'__mta=208417709.1592895912492.1592902918645.1592903952867.7; uuid_n_v=v1; uuid=DF9CCBB0B51F11EA801551553EAD9849A9C6A4B3E2894835A13DFBE0903318F2; _csrf=b440c76ad9bd8b530488f522785e6cf7af43ac1e907b9196a84bc71857d4234e; _lxsdk_cuid=172dffeb93ec8-0d64910ea0f05a-143e6257-1fa400-172dffeb93ec8; mojo-uuid=6a2c8527c33ed9dd8462351a67bb364e; mojo-session-id={"id":"5fa649bfa4a5fb40547b9af2b7ae5a30","time":1592898021553}; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172e0281287bdf-06e09e70bab7de-2076244f-546797-172e0281288c3f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172e0281287bdf-06e09e70bab7de-2076244f-546797-172e0281288c3f%22%7D; _lxsdk=DF9CCBB0B51F11EA801551553EAD9849A9C6A4B3E2894835A13DFBE0903318F2; lt=sbcAoSSv2aNOkmQO1M30XtzxY4oAAAAA5woAAM42swSU-Amm1PnUAOMGoyjjYbuzAnq3nio6jK_ArkGALUH-whiVT6KsP7yiYWj32g; lt.sig=ytlNcmJAcMmZ5ZqM84NQiRBdoqM; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592906608,1592906937,1592906948,1592906968; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1592906968; __mta=208417709.1592895912492.1592903952867.1592906969162.8; mojo-trace-id=50; _lxsdk_s=172e01ee84e-47c-6be-c2b%7C%7C99',
    'user-agent': user_agent}

response = requests.get(myurl,headers=header)
print(response.status_code)
bs_info = bs(response.text,'html.parser')

# 处理字符串
def parse_text(str):
    return str.strip().split('\n')[-1].strip()

movie_infos = []
for tags in bs_info.find_all('div',attrs={'class':'movie-hover-info'}):
    for tag in tags.find_all('div',attrs={'class':'movie-hover-title'}):
        for i in tag.find_all('span',attrs={'class':'hover-tag'}):
            if i.text == '类型:':
                movie_category = parse_text(i.find_parent('div').text)   # 获取节点的父节点的内容
            if i.text == '上映时间:':
                movie_date = parse_text(i.find_parent('div').text)
                movie_title = i.find_parent('div').get('title')      # 获取父节点的 属性内容
                movie_info = [movie_title,movie_category,movie_date]
                movie_infos.append(movie_info)

# 通过 pandas 转csv，只存10个电影即可
df = pd.DataFrame(movie_infos[:10],columns=['movie-title', 'movie-category', 'movie-date'])
df.to_csv('./movie1.csv',encoding='utf8',index=False,header=False)


