"""
作业一：

区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

list
tuple
str
dict
collections.deque
作业二：
自定义一个 python 函数，实现 map() 函数的功能。

作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。 
"""

# 作业一：
""" 
容器序列：list、tuple、dict、collections.deque
扁平序列：str
"""

# 作业二：
from collections.abc import Iterable

def n_map(func,items):
    if  isinstance(items,Iterable):
        for item in items:
            yield func(item)
    else:
        raise TypeError('请输入序列对象')
        
def square(x):
    return x**2
m = n_map(square,(2,3))
# print(next(m))
# print(next(m))
print(list(m))


# 作业三
import time
# 方式一
def timer(func,*args,**kwargs):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        run_time = end - start
        print(f'{func.__name__}运行时间: {run_time}')

    return wrapper

@timer
def test(s):
    time.sleep(s)

test(5)

# 方式二
from functools import wraps
def timer2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        run_time = end - start
        print(f'{func.__name__}运行时间: {run_time}')

    return wrapper

@timer
def test2(a,b,s):
    time.sleep(s)
    return a+b

test2(5,6,5)