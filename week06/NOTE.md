## W6 Notes

#### 1.开发环境配置

Web框架普遍遵循 MTV 框架模式。

![image-20200725204557866](https://tva1.sinaimg.cn/large/007S8ZIlgy1gh3i8lear2j31lm0q2kab.jpg)

`Django` 是应用最广的python web 框架。

- 采用 `MTV` 框架

- 强调快速开发和代码复用 `DRY（DO NOT REPEAT YOURSELF）`

- 组件丰富

  - `ORM`（对象关系映射）映射类来构建数据模型
  - `URL` 支持正则表达式
  - 模板可继承
  - 内置用户认证，提供用户认证和权限功能
  - `admin` 管理系统
  - 内置表单模型、`Cache` 缓存系统、国际化系统等

  目前最常用的 `Django` 版本为 `2.2.13`

  `pip install --upgrade django==2.2.13`

#### 2.创建项目和目录结构

创建项目：`django-admin startproject MyDjango`

项目中的app需要用 `manage.py`去创建 `python manage.py startapp index`

整个项目中，项目和app 直接是通过 `urls.py` 联系起来的

运行项目，`pyton manage.py runserver` 就可以根据提示进入页面了

主要文件：

- `models.py`
- `views.py`

`python manage.py runserver` 默认 `127.0.0.1：8000`

可以在运行的时候添加端口 `python manage.py runserver 0.0.0.0:80`

> 这里的 `0.0.0.0`代表所有 ip 都可以访问，
>
> 需要在 配置中 添加 `ALLOWED_HOSTS = ['*']`
>
> 浏览器中不要用 `0.0.0.0` 去访问。
>
> 在内网中找到电脑的ip地址，把这个地址输入 同网的手机或者电脑中，就可以打开 Django的页面了。

#### 3.解析 settings.py主要配置文件

`Django` 项目的入口在 `manage.py`，配置在 `settings.py`。

定义哪里作为`url`的入口

调试模式仅用于开发，如果是生产模式，可以添加 WSGI配置，后续课程。

自带应用不要随便去改顺序

中间件请求也是从上到下，返回是从下到上

`INSTALLED_APPS` 这里，如果有自己创建的 `app`，需要手动加入，比如 `index`

模板引擎可以用 `Django` 自带的，也可以用第三方的

指定数据库，默认 `Sqlite`，一般换成自己的数据库配置

如果使用 `mysql` 作为数据库，因为更换了驱动引擎 `django.db.backends.mysql`

使用 `pymysql` 实现这个驱动引擎

配置文件主要更改：

- 添加的 app
- 添加 数据库配置

**错误记录1**：`django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.`

解决：在 `__init__.py`中加入 

```python
import pymysql
pymysql.install_as_MySQLdb()
```

**错误记录2**：`django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.`

解决：

根据提示，到 `anaconda3/lib/python3.7/site-packages/django/db/backends/mysql/base.py", line 36, in <module>`

中将下面的配置注释：

```python
# if version < (1, 3, 13):
#     raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```

**错误记录3** `AttributeError: 'str' object has no attribute 'decode'`

按报错找到 `python3.7/site-packages/django/db/backends/mysql/operations.py", line 146,` 改成下面的就可以了

```python
#query = query.decode(errors='replace')
query = query.encode('utf-8').decode(errors='replace')
```

在第9节里面给出的解决办法是直接把这句注释掉，也可以。

这个保存是因为`python`版本的原因

#### 4.urls调度器

**URLconf** 接收请求信息，附带`Django`一些信息

控制请求返回流程，这个过程需要清晰理解

当一个用户请求Django站点的一个页面：

1. 如果传入 `HttpRequest` 对象拥有 `Urlconf` 属性（通过中间件设置），它的值将被用来替代 `ROOT_URLCONF` 设置。
2. Django 加载`Urlconf` 模块并寻找可用的 `urlpattens`，`Django` 依次匹配每个 URL 模式，在与请求的 `URL` 匹配的第一个模式停下来。
3. 一旦有 `URL` 匹配成功，`Django` 导入并调用相关的视图，视图会获得如下参数：
   - 一个 `HttpRequest` 实例
   - 一个或多个位置参数提供
4. 如果没有 `URL` 被匹配，或者匹配过程中出现了异常，`Django` 会调用一个适当的错误处理视图

#### 5.模块和包

模块是封装好的单个 py 文件

包是多个模块 py 文件放在一起的一个文件夹

#### 6.让URL支持变量

变量需设定类型

`path('<int:year>',views.myyear)`

#### 7.URL正则和自定义过滤器

正则是可以提取到类型中的实现自定义规则匹配，使用 `register_converter` 转换

`re_path('(?P<year>[0-9]{4}).html',views.myyear,name='urlyear')`

- `re_path` 含有正则的 path
- ?P 告诉 `re_path` 后面的变量和匹配的正则
- `views.myyear` 定义 view
- `name='urlyear'` 作用：`views` 中 `myyear` 返回的内容中可以引用 `urlyear`

自定义过滤器：

替代上面的 `re_path` 更简洁

```python
# index/urls.py
# 添加  register_converter
from django.urls import path ,re_path,register_converter
# 添加 converters
from . import views,converters

register_converter(converters.IntConverter,'myint')
register_converter(converters.FourDigitYearConverter,'yyyy')

# touch index/converters.py 
# 格式是固定的，规则、 to_python, to_url
class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value

```



#### 8.view视图快捷方式

`Response`、`render` 返回的结果不同

`Response`主要处理请求，也可以跳转到其他页面处理 `HttpResponseRedirect`

常用的返回做2次封装的时候，可以用快捷函数，主要有：

- `render()` 将模板文件与 `view` 视图做了绑定

  - 在 `settings.py`中 有 `template` 的配置，`'APP_DIRS': True,`在 app 内查找 模板文件

- `redirect()` 重新解析 `url` 

  - ```
    def year(request,year):
        # return HttpResponse(year)
        # 当请求的时候返回一个 html
        return redirect('/2020.html')
    ```

    

- `get_object_or_404()`



#### 9.使用ORM创建数据表

`model` 主要做数据处理，增删改查的处理。

`dgjango` 并不是直接操作数据库，而是做了一个对象的提取

每个模型都是 `python` 的类，这些类继承 `django.db.models.Model`

类的名称变成表的名称，类的属性成为表的字段。

利用这些，`Django`提供了一个自动生成访问数据库的API

#### 10.ORM API

使用 `ORM`定义的API操作 `SQL`

2个步骤：

1. 必要条件，转化为 Django能够认识的 ORM 语句，执行语句的时候才能变成SQL
   1. `python manage.py makemigrations`
   2. 执行后在 `index/migrations`中会生成中间文件
      1. `0001_initial.py`
      2. 以后每次执行都会生成对应的文件
2. 执行中间语句
   1. `python manage.py migrate`,会执行刚才生成的中间文件，也会生成一些执行记录，这些记录也在 `index/migrations`文件夹内
   2. 去 `mysql` 中可以看到生成的表
   3. ![image-20200802160454558](https://tva1.sinaimg.cn/large/007S8ZIlgy1ghcj2m1y4vj30da0h2n0d.jpg)

在 django 文档中，需要熟练掌握 模型字段类型，常用的 

- 整数 `IntegerField`
- 浮点数 `FloatField`
- 字符 `CharField`
- 日期 `DataField`

##### Django  shell 的ORM 操作

`python manage.py shell`

```python
>>> from index.models import *
>>> n = Name()
>>> n.name='红楼梦'
>>> n.author='曹雪芹'
>>> n.stars=9.6
>>> n.save()
#使用ORM框架api实现
#增
>>> from index.models import *
>>> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')
>>> Name.objects.create(name='活着', author='余华', stars='9.4')


#查
>>> Name.objects.get(id=2).name

#改
>>> Name.objects.filter(name='红楼梦').update(name='石头记')

#删 
#单条数据
>>> Name.objects.filter(name='红楼梦').delete()
#全部数据
>>> Name.objects.all().delete()

#其他常用查询
>>> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')
>>> Name.objects.create(name='活着', author='余华', stars='9.4')
>>> Name.objects.all()[0].name
>>> n = Name.objects.all()
>>> n[0].name
>>> n[1].name

>>> Name.objects.values_list('name')
<QuerySet [('红楼梦',), ('活着',)]>
>>> Name.objects.values_list('name')[0]
('红楼梦’,)
#filter支持更多查询条件
filter(name=xxx, id=yyy)

#可以引入python的函数
>>> Name.objects.values_list('name').count()
2

```



#### 11.Django模板开发

呈现给用户的最终状态的前端文件放在模板 `Templates` 里面。

模板和 `Django` 交互，用 `Django`自带的模板语言。

#### 12.展示数据库中的内容

传递数据的时候可以使用 `locals()`将本地变量都传递过去，就不用一个个传了。

views 中的数据可以用 ORM 的方式传入

```python
def books(request,):
    n= Name.objects.all()
    return render(request,'booklists.html',locals())
```



#### 13.豆瓣页面展示功能的需求分析

需要考虑展示什么数据，在什么 url 展示

1. `MTV`组合，`Models` 数据是怎么来去做的模型
2. `View` 具体取出哪些信息
3. `Template` 怎么去结合前端的框架，需要填充什么样的数据进来。
4. 如何进到这个页面 ？通过 `Urlconf`
5. 得到这些大概信息后，才开始正式写代码

#### 14.`urlcon`与`models`配置

如果功能比较简单，可以一个 页面，一个app去实现。

复杂的话，要拆分成多个，通过 `Urlconf`去处理。

如果数据库内容已经存在，可以使用  `python manage.py inspectdb > models.py` 反向输入 `models` 内容。

注意配置文件中数据库文件需要对应好。

#### 15.views视图的编写

需要用到的模型层自带的管理器，可以去官方文档里面查看。

高级功能：聚合 `aggregate` 需要用到高级函数：

`from django.db.models import AVG`进行平均值计算。

filter 的条件有固定的格式 `sentiment__gte` 双下划线将字段和条件隔开：

- `gt` ＞
- `gte`≥
- `lt`＜
- `lte`≤

#### 16.结合bootstrap模板进行开发

`Bootstrap` 是一个前端模板框架，内置格栅系统对页面进行了自适应。

可以将 `views` 中的变量传进 `html` 页面中进行展示。

#### 17.如何阅读Django的源代码

为什么要阅读源代码：

- 解决文档中没有描述的特定问题。
- 二次开发
- 学习语言——代码风格、规范、高级语法
- 学习设计模式——接口、框架、架构
- 学习算法
- 阅读源代码不是唯一的学习手段，也不是最高效的那个。

阅读源代码一般从入口处：

- 一个典型的 `python` 入口：`if __name__ = '__main__'`

#### 18.manage.py源码分析

1. `manage.py` 解析了`runserver` 和 IP 端口参数。
2. 找到 `command` 目录加载 `runserver.py`。
3. 检查 `INSTALL_APP`、IP地址、端口、`ORM`对象。
4. 实例化 `wsgiserver`。
5. 动态创建类并接受用户请求。