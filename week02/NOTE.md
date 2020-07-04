### 本周学习记录

#### mysql 数据库操作

需要机器上先安装 mysql 并启动 mysql 才可以使用。

在 python 中调用需要用的 `pymysql` 包。

#####  错误记录1 pymysql.err.InternalError:(1049,"Unknown database 'test'")

直接运行 `2d` 分支 `p1_pymysql.py` 报错：

![image-20200704130110370](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggeusgqfizj30rw01a0tt.jpg)

在数据库中操作 

![image-20200704130140807](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggeuszi1dyj30p20hk0wl.jpg)

发现没有显示，问了助教，发现是少打了分号。

![image-20200704130155273](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggeut8srxrj30tw0fgtep.jpg)



重新执行代码没有报错。

![image-20200704130212343](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggeutj61jnj30ta192k7h.jpg)



#####  错误记录2 pymysql.err.ProgrammingError: (1146, "Table 'test.tb1' doesn't exist")

在 mysql 命令行中执行 

![image-20200704130239790](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggeuu0h5r3j30l005eac4.jpg)

创建 tb1 表

然后 通过 pymysql 插入：

```python
"""  
使用 pymysql 插入数据
在 mysql 中先执行创建表命令 ceate table tb1( id int(10),name char(20));

"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='gold2020',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `tb1` (`id`, `name`) VALUES (%s, %s)"
        cursor.execute(sql, ('1', 'tom'))
        cursor.execute(sql, ('2', 'jery'))
        ```
        sql = "INSERT INTO `tb1` (`id`, `name`) VALUES (%s, %s)"
        # 执行批量插入
        values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
        cursor.executemany(sql, values)
        ```

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `name` FROM `tb1` WHERE `id`=%s"
        cursor.execute(sql, ('2',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
```



#### 模拟浏览器头部信息

##### 浏览器基本行为

1. 带http header 信息：如 `User-Agent`,`Referer` 等

2. 带 `cookies`(包含加密的用户名，密码验证信息)



模拟浏览器头部：

1. 自己 F12 看 header

2. 网络上的 header 大全

3. `fake_useragent`

4. `referer` 验证

5. 要登录才可以的 `cookie`

6. 请求是加密的，用 `webdriver` 

#### cookies验证

可以直接复制，如果爬虫规模大的话，比较麻烦，而且 cookies 普遍有有效期，如果爬虫是 7X24 就比较麻烦。

所以可以用模拟登录的方式解决。用 `post` 请求。



#### 使用 webdrive 模拟浏览器行为

网页链接加密，需要看 javascript 代码，但是可以通过点击获取页面的时候，

可以通过 webdrive 模拟用户点击的行为来获取页面信息。

需要安装：

1. `selenium`

2. `chromedrive`r，安装完需要放到 python 的路径里面

补充了小文件下载和大文件分块下载的内容

#### 验证码识别

需要安装的库：

\* `brew install leptonica`

\* `brew install tesseract`

\* `pip install Pillow`

\* `pip install pytesseract`



#### 爬虫中间件

**这节内容有点难，需要反复听**

在 scrapy 中 settings 中 设置中间件，默认是注释状态，可以通过更改后面的参数大小来调整调用的优先级，暂时不需要的可以设置 `None`

```python
DOWNLOADER_MIDDLEWARES = {

   'proxyspider.middlewares.ProxyspiderDownloaderMiddleware': 543,

    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,

    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,

}
```



##### Downloader Middlewares

下载中间件可以在请求前添加浏览器 header 和 cookies，也可以更改代理 IP

同一个 IP 去做请求的时候，并发的数据量大，会被反爬虫。

代理 IP 可以通过：

方式一：系统代理设置 

export http_proxy='http://52.179.231.206:80'` 临时加载 

方式二：settings 中配置，需要重写代理中间件，有4个主要方法

```
process_request(request,spider)
```

`Request` 对象经过下载中间件时会被调用，优先级高的优先调用

```
process_response(request,response,spider)
```

`Response` 对象经过下载中间件时会被调用，优先级高的后调用

```
process_exception(request,exception,spider)
```

当 `process_exception` 和 `process_request()` 抛出异常时会被调用

```
from_crawler(cls,crawler)
```

使用 `crawler` 来创建中间器对象，并（必须）返回一个中间件对象



##### 分布式爬虫

需要用到 `redis`

##### 补充内容

一、`scrapy crawl httpbin --nolog`

可以让 scrapy 输出的内容 不再显示 Log内容

二、 `collections.defaultdict` 是什么？

它的初始化函数接受一个类型作为参数，就如演示代码中的 `defaultdict(list)` 一样。

当所访问的键不存在的时候，可以实例化一个值作为默认值。

说人话就是，一个会报错一个不会，如下图

```python
>>> a = {}

>>> a['foo']

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

KeyError: 'foo'

>>> *from* collections *import* defaultdict

>>> b = defaultdict(list)

>>> b['bar']

[]

>>> 
```

#### 作业过程错误记录

先感觉助教的耐心指导。

##### 错误1 在爬虫文件可以打印，`pipelines.py` 中打不出来

![image-20200704131133876](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggev3boiohj313o0que09.jpg)



可以先通过 `print('*'100)`来确认 `pipelines` 正常，最后发现是 `settings.py` 中 

```python
ITEM_PIPELINES = {
    'doubanmovie.pipelines.DoubanmoviePipeline': 300,
}

```

这个没有去掉注释造成的

##### 错误2 设置了代理仍然被反爬

代理设置的有问题，爬 https 应该用 https代理。用 http 代理是不行的，而且最好多写几个代理，随机选。

需要经常到 爬虫文件中 `print(response.text)`查看返回的 html 是否正确来确认是否被反爬

##### 错误3 电影简介和标题对不上

![611593831814_.pic_hd](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggev7zgqeej30wo0u0k2q.jpg)

![681593832139_.pic_hd](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggev86cop8j313u0u00y4.jpg)

这里是因为数据结构问题，改成下面的就可以了。

**要经常注意数据问题，需要的数据是什么样的，当有循环的时候，检查输出的数据是否符合需求**。

![781593837263_.pic](https://tva1.sinaimg.cn/large/007S8ZIlgy1ggev8k2h5ij316s0ecac9.jpg)