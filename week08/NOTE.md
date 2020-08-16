## W8 Note

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





