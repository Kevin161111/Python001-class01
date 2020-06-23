## Week01 学习笔记

#### 主要内容

从最简单的 `Requsets` 发起最简单的爬虫，进阶到 `BeautifulSoup`、 `XPath` 解析网页，实现简单版的爬虫。

到用 `Scrapy` 框架爬虫，用框架也是不是上来就直接操作的，而是先学习了这个框架的基本内容，文件都是用来做什么的，然后搭配上面的三个包，实操中完成框架学习，和之前包的复习。

中间穿插了 生成器、`yield` 关键字的作用

#### 课程方式

用视频录播讲解的形式进行。

老师讲课比较有条理，结构清晰。

需要理解的重点和后续要展开的都说的比较清楚。

#### 作业中遇到的问题及解决

##### 返爬

作业1，爬取猫眼电影网址的时候出现了第一次可以，后面几次都出现了验证中心，等了半个小时可以了，但是写代码的过程中不行了，一直出现验证中心的返回，不能得到正确的 `response` 。去作业群问了助教了解到可能是限制了。

google 解决办法，尝试 proxy代理池，出现问题，链接不上代理池，可能免费的代理有问题。

尝试 fake-user_agent 没什么用，应该是限制了ip。

尝试 加入 cookies，登录网址有，将请求的 `header` 中 `cookies` 内容复制到代码中，添加到 `header` 中，解决问题。

##### scrapy 反爬

1、`settings.py` 中 添加 `COOKIES_ENABLED = True`

2、添加到爬虫文件中
```python
# movies.py

from http.cookies import SimpleCookie
cookies_fromchrome = '贴进去从 chrome 复制的 cookie'

cookie = SimpleCookie(cookies_fromchrome)
cookies = {i.key:i.value for i in cookie.values()}

# 将cookies添加到 scrapy.Request中
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse,dont_filter=False,cookies=self.cookies)

```