## W8 Notes

#### 1、变量赋值

python 中的类型非常丰富，导致变量赋值简单操作也会变的很复杂。

需要注意的点：

```python
# 问题4: a、b的值分别是多少
a = [1, 2, 3]
b = a
a = [4, 5, 6]
# a,b 不同

#############
# 问题5: a、b的值分别是多少
a = [1, 2, 3]
b = a
a[0],a[1],a[2] = 4, 5, 6
# a,b相同
```

python 中一切皆对象，只是有的传递的是对象本身，有的传递的是对象的引用。

##### 变量赋值

可变数据类型：传的是数据的引用，传的是对象的地址。**对可变类型的修改会影响变量的取值**。

- list
- dict

不可变数据类型：传的是数据本身，大量创建的时候会消耗多的内存。

- int
- float
- string
- Tuple

> 补充：set是可变数据类型，frozenset是不可变数据类型

#### 2、容器序列的深度拷贝

序列分类：

- 容器序列：list、tuple、collections.deque等，能存放不同类型的数据 容器序列可以存放不同类型的数据。
- 扁平序列：str、bytes、bytearray、memoryview(内存视图)、array.array等，存放的事相同类型的数据，扁平序列只能容纳一种类型。

容器序列存在深拷贝、浅拷贝的问题：

- 注意：**非容器(数字、字符串、元祖)类型没有拷贝问题**。

如下所示：

`list()` 和 `[:]`操作会创建新的内存地址，和原来的容器已经独立。

```python
import copy
copy.copy(obj)
copy.deepcopy(obj)

# 容器序列的拷贝问题

old_list = [ i for i in range(1, 11)]

new_list1 = old_list
new_list2 = list(old_list)

# 切片操作
new_list3 = old_list[:]

# 嵌套对象
old_list.append([11, 12])

import copy
new_list4 = copy.copy(old_list)  # 浅拷贝
new_list5 = copy.deepcopy(old_list) # 深拷贝

assert new_list4 == new_list5 #True
assert new_list4 is new_list5 #False AssertionError

old_list[10][0] = 13
```

#### 3、字典与扩展内置数据类型

字典的 Hash 关系的好处：

- 因为是映射关系，可以快速取到某个元素，list 的话要一个个去找
- 只有不可变的数据类型才可以 hash，才能用作 key

##### `Collections` 扩展内置数据类型

- `namedtuple`带命名的元组

  - ```python
    from collections import namedtuple
    Point = namedtuple('Ponit', ['x','y'])
    p = Point(10, y=20)
    p.x + p.y
    p[0] + p[1]
    x, y =  p # 神奇
    ```

    

- `Counter`

  - ```python
    from collections import Counter
    mystring = ['a','b','c','d','d','d','d','c','c','e']
    # 取得频率最高的前三个值
    cnt = Counter(mystring)
    cnt.most_common(3)
    cnt['b']
    ```

    



* `deque`双向队列

  * ```python
    from collections import deque
    d = deque('uvw')
    d.append('xyz')
    d.appendleft('rst')
    ```

#### 

#### 4、函数

函数需要关注的点：函数的调用、作用域、参数、返回值。

#### 5、变量的作用域

高级语言对变量的使用：

- 变量声明
- 定义类型（分配内存空间大小）
- 初始化（赋值、填充内存）
- 引用（通过对象名称调用对象内存数据）

python 和高级语言有很大差别，在模块、类、函数中定义，才有作用域的概念。

由于python 的动态性，不像其他语言那样定义了类型，近期版本中出现了 `Type Hint` 。

了解作用域的目的：

- 如果你的变量名是同名的，但是在不同作用域，可能会有问题
- 同名不同作用域的时候，查找顺序也是会影响程序运行的。

Python 作用域遵循 LEGB 规则：

- `L-Local(function)` 函数内的作用域

- `E-Enclosing function locals` 外部嵌套函数的作用域（例如 closure 闭包）

  - 闭包是一种特殊的代码结构，理解代码的时候一定要注意返回值和函数的调用执行

  - 内部函数对外部函数作用域变量的引用（非全局变量），则称内部函数为闭包

  - ```python
    def func4():
        x = 'Enclosing'
        def func5():
            return x
        return func5
    var = func4()
    print(var())
    ```

  - 闭包最大的作用是去做装饰器

- `G-Global(module)`函数定义所在模块（文件）的作用域

- `B-Builtin(python）` Python 内置模块的作用域

#### 6、函数工具与高阶函数

动态参数与处理，关注传入参数的对象类型，字典与序列类型。

- `*args` 序列参数
- `**kwargs` 关键字参数

内部传递的时候，有传递顺序的问题，注意关键字参数放后面。

##### 偏函数 partial

返回一个可调用的`partial`对象，`partial(func,*args,**kw)`

- `func`为必须参数

- 至少需要一个`args` 或`kw` 参数

- ```python
  from functools import partial
  def add(x,y):
    	return x +y
  add_1 = partial(add,1) # add(1,y):return 1 +y
  add_1(10) 相当于执行  1+10
  ```

- 

固定函数的某些参数，前几个固定的话，每次都需要传入的话，可以处理成偏函数。

需要第5个参数的时候，直接传第5个即可。

这个功能很常用。

##### 高阶函数

函数的参数也是函数，就是高阶函数，也用于函数式编程。

基本都可以用 Lambda 表达式。

Lambda 表达式，不是所有的函数逻辑都能封装进去。它只能有一个表达式。

- 实现简单函数的时候可以用 `Lambda` 表达式替代
- 使用高阶函数的时候一般是用 `Lambda` 表达式

高阶：参数是函数 ，返回值也是函数

常见的高阶函数：`map`、`reduce`、`filter`、`apply`

`apply` 在 Python2.3 被移除，`reduce` 被放在 `functools` 中

推导式和生成器表达式可以替代 `map` 和 `filter` 函数。

```python
#map
def square(x):
  	return x**2

m = map(square,range(10)) #返回值是迭代器的方式
next(m)
list(m) # 通过list 展开
[square(x) for x in range(10)] 

# reduce
# reduce(f,[x1,x2,x3]) = f(f(x1,x2),x3)
from functools import reduce
def add(x,y):
  	return x + y
reduce(add,[1,3,5,7,9]) # 返回一个具体值 25

# filter
def is_odd(n):
  	return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
```

官方文档中的 `functools` 和 `itertools` 需要掌握常用的几个高阶函数。

#### 7、闭包

##### 返回值

返回关键字：`return` ,`yield`

返回的对象：可调用对象--闭包（装饰器）

内部函数对外部函数作用域变量的引用（非全局变量），则称内部函数为闭包

可以通过关键字查询编译后函数保存的变量：

```python
# 编译后函数体保存的局部变量
print(my_line.__code__.co_varnames)
# 编译后函数体保存的自由变量，外部变量
print(my_line.__code__.co_freevars)
# 自由变量真正的值
print(my_line.__closure__[0].cell_contents)
```

通过打印出来的局部变量、外部变量的值可以知道，内部函数可以对外部函数的变量形成闭包。这样做的好处可以实现外部函数定义的变量不受 global 同名变量的影响。

直观的好处可以通过下面的代码体会：

```python
a = 100
b = 200
def line_conf(a,b): # closure a,b 与外部无关
    def line(x):
        return a*x + b
    return line
line1 = line_conf(1,1) # 只需要定义 a,b即可定义1条线
line2 = line_conf(4,5)
print(line1(5),line2(5))
```

#### 8、装饰器

装饰器其实是一种设计模式，不改变原有属性，而是去增加属性。增强而不改变原有函数。

强调函数的定义态而不是运行态，底层是通过闭包实现的。

也就是说 装饰器函数写完，装饰到被装饰器函数上的时候，已经被执行。被装饰器函数在定义的时候就已经被装饰器改变了。

```python
@decorate
def target():
  	print('do something')
    
def target():
  	print('do something')
target = decorate(target)
```

#### 9、被装饰函数带参数和返回值的处理

```python
def outer(func):
    def inner(a,b):
        print(f'inner: {func.__name__}')
        print(a,b)
        func(a,b)
    return inner

@outer
def foo(a,b):
    print(a+b)
    print(f'foo: {foo.__name__}')
    
    
foo(1,2)
foo.__name__

inner:foo
1 2
3
foo: inner
```

注意这段代码的执行顺序

1. `foo = outer(foo)`
2. `foo = inner(1,2)`
3. `print  inner:foo` 
4. `print 1 2`
5. `func(a,b) = foo(1,2)`
6. `print 3`
7. `print foo.__name__` 即 print inner

被装饰函数带参数的时候，内部函数也要带同样的参数，且传入原有的 foo 的函数 `func(a,b)`

如果是不定长参数，可以将 内部函数和原有参数都改下：

```python
# 被修饰函数带不定长参数
def outer2(func):
    def inner2(*args,**kwargs):
        func(*args,**kwargs)
    return inner2
@outer2
def foo2(a,b,c):
    print(a+b+c)
    
foo2(1,3,5)
```

如果被装饰函数带返回值

```python
def outer3(func):
    def inner3(*args,**kwargs):
        ###
        ret = func(*args,**kwargs) # 将调用函数的返回值接收并返回
        ###
        return ret
    return inner3

@outer3
def foo3(a,b,c):
    return (a+b+c)
    
print(foo3(1,3,5))
```

实现装饰器带参数

```python
def outer_arg(bar):
    def outer(func):
        def inner(*args,**kwargs):
            ret = func(*args,**kwargs)
            print(bar) #打印装饰器函数的参数
            return ret
        return inner
    return outer

# 相当于outer_arg('foo_arg')(foo)()
@outer_arg('foo_arg')
def foo(a,b,c):
    return (a+b+c)
    
print(foo(1,3,5))

```

装饰器也可以堆叠，注意执行的顺序

```python
@classmethod
@synchronized(lock)
def foo(cls):
    pass


def foo(cls):
    pass
foo2 = synchronized(lock)(foo)
foo3 = classmethod(foo2)
foo = foo3
```

#### 10、python内置的装饰器

```python
# 保证被装饰的函数在内部还原回原来的函数
# functools.wraps
# @wraps接受一个函数来进行装饰
# 并加入了复制函数名称、注释文档、参数列表等等的功能
# 在装饰器里面可以访问在装饰之前的函数的属性
# @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 用于在定义包装器函数时发起调用 update_wrapper() 作为函数装饰器。 
# 它等价于 partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)。


from time import ctime,sleep
from functools import wraps
def outer_arg(bar):
    def outer(func):
        # 结构不变增加wraps
        @wraps(func)
        def inner(*args,**kwargs):
            print("%s called at %s"%(func.__name__,ctime()))
            ret = func(*args,**kwargs)
            print(bar)
            return ret
        return inner
    return outer

@outer_arg('foo_arg')
def foo(a,b,c):
    """  __doc__  """
    return (a+b+c)
    
print(foo.__name__)

foo
```

`functools.wraps`主要是为了保持原函数不要被装饰器内部函数替换

如果不加此装饰器，上面打印的结果就不是 `foo` 而是 `inner`,这就会造成改函数在被其他地方使用的时候造成误解。

`functools.lru_cache`缓存，使用 LRU 算法实现内存缓存和释放

```python
# functools.lru_cache
# 《fluent python》的例子
# functools.lru_cache(maxsize=128, typed=False)有两个可选参数
# maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放
# typed若为True，则会把不同的参数类型得到的结果分开保存
import functools
@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    import timeit
    print(timeit.timeit("fibonacci(6)", setup="from __main__ import fibonacci"))
```

#### 11、类装饰器

要实现类做装饰器，类中需要实现 `__call__`方法，其余和普通的装饰器函数相同。

好处是，用类做装饰器的话方便传递参数，实现装饰器函数带参数的功能。

```python
from functools import wraps

class MyClass(object):
    def __init__(self, var='init_var', *args, **kwargs):
        self._v = var
        super(MyClass, self).__init__(*args, **kwargs)
    
    def __call__(self, func):
        # 类的函数装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__ + " was called"
            print(func_name)
            return func(*args, **kwargs)
        return wrapped_function

def myfunc():
    pass

MyClass(100)(myfunc)()
# 其他经常用在类装饰器的python自带装饰器
# classmethod
# staticmethod
# property


# 另一个示例
class Count(object):
    def __init__(self,func):
        self._func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kargs):
        self.num_calls += 1
        print(f'num of call is {self.num_calls}')
        return self._func(*args, **kargs)

@Count
def example():
    print('hello')

example()
print(type(example))
```

装饰器也是可以装饰类的

```python
# 装饰类
def decorator(aClass):
    class newClass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aClass(args)
            
        def display(self):
            # 将runtimes()替换为display()
            self.times += 1
            print("run times", self.times)
            self.wrapped.display()
    return newClass

@decorator
class MyClass(object):
    def __init__(self, number):
        self.number = number
    # 重写display
    def display(self):
        print("number is",self.number)

six = MyClass(6)
for i in range(5):
    six.display()
```

#### 12、官方文档中的装饰器代码阅读指南

通过阅读官方文档，可以了解版本更新，主要是 PEP 文档的更新。

读懂官方文档，可以了解更新内容的使用场景。

```python
# 向一个函数添加属性
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate

@attrs(versionadded="2.2",
       author="Guido van Rossum")
def mymethod(f):
    pass

##############################

# 函数参数观察器
import functools
def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function
@trace
def greet(greeting, name):
    return '{}, {}!'.format(greeting, name)

greet('better','me')


############################################

# Python3.7 引入 Data Class  PEP557

class MyClass:
    def __init__(self, var_a, var_b):
        self.var_a = var_a
        self.var_b = var_b

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return False
        return (self.var_a, self.var_b) == (other.var_a, other.var_b)
        
var3 = MyClass('x','y')
var4 = MyClass('x','y')

var3 == var4

from dataclasses import dataclass
@dataclass
class MyClass:
    var_a: str # Type Hint 类型提示符
    var_b: str

var_1 = MyClass('x','y')
var_2 = MyClass('x','y')

# 不用在类中重新封装 __eq__

var_1 == var_2
# 存在的问题: var_a var_b不能作为类属性访问

##########################

# 如下的类装饰器实现了一个用于类实例属性的Private声明
# 属性存储在一个实例上，或者从其一个类继承而来
# 不接受从装饰的类的外部对这样的属性的获取和修改访问
# 但是，仍然允许类自身在其方法中自由地访问那些名称
# 类似于Java中的private属性

traceMe = False
def trace(*args):
    if traceMe:
        print('['+ ' '.join(map(str,args))+ ']')

def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self,*args,**kargs):
                self.wrapped = aClass(*args,**kargs)
            def __getattr__(self,attr):
                trace('get:',attr)
                if attr in privates:
                    raise TypeError('private attribute fetch:'+attr)
                else:
                    return getattr(self.wrapped,attr)
            def __setattr__(self,attr,value):
                trace('set:',attr,value)
                if attr == 'wrapped': # 这里捕捉对wrapped的赋值
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change:'+attr)
                else: # 这里捕捉对wrapped.attr的赋值
                    setattr(self.wrapped,attr,value)
        return onInstance
    return onDecorator

if __name__ == '__main__':
    traceMe = True

    @Private('data','size')
    class Doubler:
        def __init__(self,label,start):
            self.label = label
            self.data = start
        def size(self):
            return len(self.data)
        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s'%(self.label,self.data))

    X = Doubler('X is',[1,2,3])
    Y = Doubler('Y is',[-10,-20,-30])
    print(X.label)
    X.display()
    X.double()
    X.display()
    print(Y.label)
    Y.display()
    Y.double()
    Y.label = 'Spam'
    Y.display()

    # 这些访问都会引发异常
    print(X.size())
    print(X.data)
    X.data = [1,1,1]
    X.size = lambda S:0
    print(Y.data)
    print(Y.size())

# 这个示例运用了装饰器参数等语法，稍微有些复杂，运行结果如下：
# [set: wrapped <__main__.Doubler object at 0x03421F10>]
# [set: wrapped <__main__.Doubler object at 0x031B7470>]
# [get: label]
# X is
# [get: display]
# X is => [1, 2, 3]
# [get: double]
# [get: display]
# X is => [2, 4, 6]
# [get: label]
# Y is
# [get: display]
# Y is => [-10, -20, -30]
# [get: double]
# [set: label Spam]
# [get: display]

```



#### 13、对象协议与鸭子类型

对象协议是一种对象之间沟通的语言，我要的东西你有，协议就达成

python 中实现对象协议用的魔术方法。

鸭子方法：如果我能用字典的方式调用你，我认为你就是字典。

定义的对象可以没有最初始化的初始类型的。在运行的过程中也可以改变对象的类型。

常用的魔术方法：

- `__str__`打印对象时，默认输出该方法的返回值。
- `__getitem_`、`__setitem__`、`__delitem__`、字典索引操作
- `__iter__`迭代器
- `__call__`可调用对象协议
- `__eq__`等于
- `__gt__`大于
- `__get__`描述符协议
- `__set__`属性交互协议
- `__hash__`可哈希对象
- `__with__`、`__exit__`实现上下文管理器

自己定义的数据类型尽量模拟原生的数据类型，这样会方法通用，用的人也方便。开发起来更简洁高效。

```python
class Foo(object):
    # 用与方法返回
    def __str__(self):
        return '__str__ is called'

    # 用于字典操作
    def __getitem__(self, key):
        print(f'__getitem__ {key}') 
    
    def __setitem__(self, key, value):
        print(f'__setitem__ {key}, {value}')
    
    def __delitem__(self, key):
        print(f'__delitem__ {key}')

    # 用于迭代
    def __iter__(self):
        return iter([i for i in range(5)])


# __str__
bar = Foo()
print(bar)

# __XXitem__
bar['key1']
bar['key1']='value1'
del bar['key1']

# __iter__
for i in bar:
    print(i)


```

#### 14、yield

生成器：

1. 在函数中使用 `yield` 关键字，可以实现生成器,如果有 `yield` ，函数被调用后 type 会变成 `<class 'generator'>`
   1. `(i for i in range(5))` 就是 `generator`
2. 生成器可以让函数返回可迭代对象
3. `yield` 和 `return` 不同， `return` 返回后，函数状态终止，`yield` 保持函数的执行状态，返回后，函数回到之前保存的状态继续执行。
4. 函数被 `yield` 会暂停，局部变量也会被保存
5. 迭代器终止时，会抛出 `StopIteration` 异常。

|    类型     | 包含内容                                     | 别名       |
| :---------: | -------------------------------------------- | ---------- |
| `Iterables` | 包含`__getitem__`或 `__iter__`方法的容器对象 | 可迭代对象 |
| `iterator`  | 包含 `next()`和 `__iter__`方法               | 迭代器     |
| `Generator` | 包含 `yield` 语句的函数                      | 生成器     |

结论一：列表是可迭代对象，或称作可迭代 `iterable`，不是迭代器 `iterator`

结论二：只要一个函数的定义中出现了 yield 关键字，则此函数将不再是一个函数，而成为一个 「生成器构造函数」，调用此构造函数即可产生一个生成器对象。

```python
def check_iterator(obj):
    if hasattr( obj, '__iter__' ):  
        if hasattr( obj, '__next__' ):
            print(f'{obj} is a iterator') # 完整迭代器协议
        else:
            print(f'{obj} is a iterable') # 可迭代对象
    else:
        print(f'{obj} can not iterable') # 不可迭代

def func1():
    yield range(5)

check_iterator(func1)
check_iterator(func1())
```

#### 15、迭代器使用的注意事项

迭代器会把变量暂存到内存中，并不会节省内存。

实现了迭代器协议，可以用 `next`去调用里面的元素。

```python
# itertools的三个常见无限迭代器
import itertools

count = itertools.count()  # 计数器
next(count)
next(count)
next(count)

###############
cycle = itertools.cycle( ('yes', 'no') ) # 循环遍历
next(cycle)
next(cycle)
next(cycle)

###############
repeat = itertools.repeat(10, times=2)  # 重复
next(repeat)
next(repeat)
next(repeat)

################
# 有限迭代器，避免多次循环
for j in itertools.chain('ABC',[1, 2, 3]) :
    print(j)

# Python3.3 引入了 yield from 
# PEP-380
# 多次循环取出元素
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

s = 'ABC'
t = [1, 2, 3]
list(chain(s, t))

def chain2(*iterables):
    for i in iterables:
        yield from i   # 替代内层循环

list(chain2(s, t))
```

**迭代器操作中的注意事项**

```python
# 迭代器有效性测试
a_dict = {'a':1, 'b':2}
a_dict_iter = iter(a_dict) #通过 iter 操作将字典转换为迭代器

next(a_dict_iter)

a_dict['c']=3

next(a_dict_iter)
# RuntimeError: 字典进行插入操作后，字典迭代器会立即失效

# 尾插入操作不会损坏指向当前元素的List迭代器,列表会自动变长


# 迭代器一旦耗尽，永久损坏
x = iter([ y for y in range(5)])
# 通过for 操作将 元素都取出来，相当于耗尽
for i in x:
    i
x.__next__()
```

#### 16、yield 表达式

利用 `yield` 实现输出与输入功能

读代码的时候，在 `yield` 那将程序分上下两部分

```python
def jumping_range(up_to):
    index = 0
    while index < up_to:
        jump = yield index
        print(f'jump is {jump}')
        if jump is None:
            jump = 1   # next() 或者 send(None)
        index += jump 
        print(f'index is {index}')

if __name__ == '__main__':
    iterator = jumping_range(5)
    print(next(iterator)) # 0
    print(iterator.send(2)) # 2 # 这里是将send的值2，赋值给了 jump,并恢复了下半部分程序
    print(next(iterator)) # 3 # 执行 next 相当于 send(None),此时 jump 为 None,index为3
    print(iterator.send(-1)) # 2
    for x in iterator:
        print(x) # 3, 
        
```

`next` 和 `send` 可以实现 `yield`暂时和恢复到下一次暂停。

通过这个功能可以人工控制程序的流程，实现协程。

#### 17、协程简介

协程可以实现 IO密集型高效率操作，执行 IO 操作的时候，与其傻等，不如去执行其他的操作，当得到新的通知说IO 准备就绪了，可以进行读写了，协程再恢复。

这个过程可以用 `yield` 表达式实现。

比较下 `yield` 和 `threading`,协程和线程的区别：

- 协程是异步的，线程是同步的
- 协程是非抢占式，线程是抢占式
- 线程是被动调度的，协程是主动调度的
- 协程可以暂停函数的执行，保留上一次调用的状态，是增强型生成器
- 协程是用户级的任务调度，线程是内核级的任务调度
- 协程适用于 IO 密集型程序，不适用于 CPU 密集型程序的处理

##### 异步编程

Python 3.5 版本引入 `await` 取代 `yield from` 方式

```python
import asyncio
async def py35_coro()：
		await stuff()
```

`await` 结束的对象必须是 `awaitable` 对象

`awaitable` 对象定义了 `__await__`方法

`awaitable` 对象有三类：

1. 协程 `coroutine`
2. 任务 `Task`
3. 未来对象 `Future`

##### 事件循环

程序分配了一些事物，或者分配了一些消息的编程框架

当A事件发生的时候去执行B，只有被注册过的函数才能执行回调函数，在python中的IO操作就是注册事件。

`asyncio`只是处理网络服务过程中等对方返回，等待的过程是网络 IO 最重要的瓶颈。

发送请求，注册自己，接收到返回信息，再去找对应回调函数，进行相应的响应。

三个关键点：

1. 注册事件循环
2. 响应事件
3. 回调函数

```python
# python3.4 支持事件循环的方法
import asyncio

@asyncio.coroutine
def py34_func():
    yield from sth()

##################
# python3.5 增加async await
async def py35_func():
    await sth()

# 注意： await 接收的对象必须是awaitable对象
# awaitable 对象定义了__await__()方法
# awaitable 对象有三类
# 1 协程 coroutine
# 2 任务 Task
# 3 未来对象 Future
#####################
import asyncio
async def main():
    print('hello')
    await asyncio.sleep(3)
    print('world')

# asyncio.run()运行最高层级的conroutine
asyncio.run(main())
# 在 jupyter 中不能这么写，要直接写 await main()
# hello
# sleep 3 second
# world

#################
# 协程调用过程： 
# 调用协程时，会被注册到ioloop，返回coroutine对象
# 用ensure_future 封装为Future对象
# 提交给ioloop

# 官方文档
# https://docs.python.org/zh-cn/3/library/asyncio-task.html

```

#### 18、aiohttp简介

`asyncio`更偏向于底层，实际工作多用协程完成 HTTP 请求

可以利用 `aiohttp` 实现客户端和服务端的请求操作。

```python
# Web Server
from aiohttp import web

# views
async def index(request):
    return web.Response(text='hello aiohttp')

# routes
def setup_routes(app):
    app.router.add_get('/', index)

# app
app = web.Application()
setup_routes(app)
web.run_app(app, host='127.0.0.1', port=8080) # 启动程序，将事件循环和注册写到了一起


# 官方文档
# https://hubertroy.gitbooks.io/aiohttp-chinese-documentation/content/aiohttp%E6%96%87%E6%A1%A3/ServerTutorial.html
```

`aiohttp` 性能很好,超过很多的 异步 http 框架。

```python
# web client

import aiohttp
import asyncio

url = 'http://httpbin.org/get' # 单页面

async def fetch(client, url):
    # get 方式请求url
    async with client.get(url) as resp: # 相当于 yield
        assert resp.status == 200 # 等价于 if not resp.status == 200: raise AssertionError()
        return await resp.text()

async def main():
    # 获取session对象
    async with aiohttp.ClientSession() as client: # 产生 session 对象
        html = await fetch(client, url)
        print(html)

loop = asyncio.get_event_loop() # 初始化事件循环，空的
task = loop.create_task(main()) # 添加任务
loop.run_until_complete(task) # task 将 async main注册成一个任务，并调用
# Zero-sleep 让底层连接得到关闭的缓冲时间
loop.run_until_complete(asyncio.sleep(0))
loop.close()

# 协程调用过程： 
# 调用协程时，会被注册到ioloop，返回coroutine对象 # 20 行
# 用ensure_future 封装为Future对象 # 这里没有封装，直接调用了 task 21行，22行
# 提交给ioloop # 24行
```

多页面版本

```python
import aiohttp
import asyncio

urls = [
    'http://httpbin.org',
    'http://httpbin.org/get',
    'http://httpbin.org/ip',
    'http://httpbin.org/headers'
]

async def  crawler():
    async with aiohttp.ClientSession() as session:
        futures = map(asyncio.ensure_future, map(session.get, urls))  #封装 futures
        for task in asyncio.as_completed(futures):
            print(await task)

if __name__ == "__main__":
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asyncio.ensure_future(crawler())) #相当于启动了4个协程
    
   # 协程调用过程： 
# 调用协程时，会被注册到ioloop，返回coroutine对象 asyncio.get_event_loop()
# 用ensure_future 封装为Future对象 # 13行 futures = xxx, await task
# 提交给ioloop  # 19行，ioloop.run_until_complete
```

协程和多进程配合组成高效的 `web server`

协程在应用层使用，无法跨 cpu 核心，但是进程可以，所以结合起来用

```python
# 进程池和协程

from multiprocessing import Pool
import asyncio
import time

# 可以把 test 改成任意想要的程序
async def test(time):
    await asyncio.sleep(time)

async def main(num):
    start_time = time.time()
    tasks = [asyncio.create_task(test(1)) for proxy in range(num)]
    [await t for t in tasks]
    print(time.time() - start_time)


def run(num):
    asyncio.run(main(num)) # 每一个运行的进程中都跑了协程


if __name__ == "__main__":
    start_time = time.time()
    p = Pool()
    for i in range(4):
        p.apply_async(run, args=(2500,)) # 异步调用 run，带参数
    p.close()
    p.join()
    print(f'total {time.time() - start_time}')
```

因为在 Cpython 中 GIL 锁的问题，协程不会和多线程结合。

实际一般都是 多进程+协程，或者多进程+多线程的方式。