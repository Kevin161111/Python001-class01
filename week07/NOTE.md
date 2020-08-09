## W7 Notes

#### 1、类属性和对象属性

- 类属性在内存是只保存一份
- 对象属性在每个对象都保存一份

`类.__dict__`查看类的所有属性

`实例对象.__dict__`查看实例的对象

`实例对象.__class__()`指向当前实例的类并且实例化，如果是2个实例的类相同，这里返回的结果是不同的。需要注意。

> 比如这里的 `a.__class__`返回的其实是a的类A，`a.__class__()`相当于A(),做了实例化，在内存中的位置当然不同。 

#### 2、类的属性作用域

- `_name` 人为约定不可修改。
  - 一般是内部属性，中间值属性，参与某些运算，运算中保留这个属性。
- `__name` 私有属性。
  - 定义好后会自动改名(`Human2__fly`)，防止程序误修改。
  - 用 `__dict__`可以看到改为 `Human2__fly`。
  - 说明也是可以访问到的。
- `__name__`魔术方法。

##### 几个基本的魔术方法

- `__base__`找到父类。

- `__subclass__` 找到子类。

- 示例：

  - ```python
    # 显示object类的所有子类
    print( ().__class__.__bases__[0].__subclasses__() )
    ```

    

#### 3、类方法描述器

主要三种方法：普通方法、类方法、静态方法。

三种方法在内存中都归属于类。

##### 普通方法

给实例化之后的对象用的。

至少一个 `self`参数，表示该方法的对象。

##### 类方法

至少一个 `cls` 参数，表示该方法的类。

可以实现父类中定义类方法，子类实现自动绑定。

实例对象也可以使用类方法，自己没有方法的时候，会去类里面找，`bound method`

两大使用场景：

1. 定义到父类当中，使用子类的时候，如果需要根据情况发生变化，可以用到父类的 `classmethod`
2. 当函数需要用到类并返回类的时候，多用于数据预处理

> `classmethod` 其实是构造函数，因为原始的构造函数 `__new__()`只有一个，不能满足我们的正常需要。
>
> 所以在父类中使用类方法，来让子类初始化的时候方便处理。

##### 静态方法

由类调用，无参数

如果有一个和类相关的功能，但是不想放在别的地方，强调和类的关联，但是和类内部的属性和方法无关。

#### 4、静态方法描述器

`staticmethod`没有带绑定，不能引用类的属性和实例属性。

一般基于额外处理的逻辑，这些逻辑和类、实例不相干的时候使用。

#### 5、描述器高级应用 `__getattribute__`

描述器是实现特定协议的一种工具。

主要用于实例获取属性的行为。也可以用 `__getattr__`

- `__getattr__`适用于未定义的属性。
- `__getattribute__`对所有属性的访问都会调用该方法，在具有封装操作（私有化时)，为程序开放部分的访问权限使用。

#### 6、描述器高级应用 `__getattr__`

`__getattribute__`无论如何都会在 `__getattr__`之前触发，触发了 `__getattribute__`有返回值就不会再触发 `__getattr__`



```python
class Human2(object):   
    def __init__(self):
        self.age = 18
    def __getattribute__(self,item):
        print(f' __getattribute__ called item:{item}')
        return super().__getattribute__(item)
h1 = Human2()
```

如果访问 `h1.name`先触发 `__getattribute__`由于没有返回值，就用 `__getattr__`报错。

如果同时存在，执行顺序是 `__getattribute__ > __getattr__ > __dict__`

实际使用过程需要注意：

1. 无论是否重写 `__getattribute__`，都会去调用原生的方法，所以会对性能有一定影响。
2. 使用 `__getattr__`的时候，`__dict__`中依然没有这个属性，当使用 `hasattr`判断的时候，即使可以返回 `True`，通过 `dir`等方式依然看不到存在的属性。
3. 因为重写了这些方法，会和内置的一些方法的返回值有冲突。开发的时候如果不清楚原理，容易挖坑。

#### 7、描述器原理&属性描述符

描述符是实现特定协议的类。

属性描述符 `property` 把方法描述成属性，调用起来更简洁。

```python
# 限制传入的类型和范围（整数，且满足18-65）
class Age(object):
    def __init__(self, default_age = 18):
        self.age_range = range(18,66)
        self.default_age = default_age
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default_age)
    
    def __set__(self, isinstance, value):
        if value not in self.age_range:
            raise ValueError('must be in (18-65)')

        self.data[isinstance] = value
        print(self.data[isinstance])

class Student(object):
    age = Age()

if __name__ == '__main__':
    s1 = Student()
    s1.age = 30
    s1.age = 100
```

#### 8、面向对象编程-继承

封装、继承、重载、多态

所有的类都继承自一个基类 `Object`，

`type`类，很多类继承自 `type`类，但是有区别

- object 和 type 都属于 type 类(`class 'type'`)
- type 类由type 元类自身创建。`object` 类由 元类 type 创建
- object 的父类为空，没有继承任何类
- type 的父类为object类(`class'object'`)

```python
# __class__
# __bases__ 继承关系

>>>print('object',object.__class__,object.__bases__)
>>>print('type',type.__class__,type.__bases__)

>>>object <class 'type'> ()
>>>type <class 'type'> (<class 'object'>,)
```

误解：A创建了B，A就一定是B的父类吗？不一定。

创建和继承是两个概念， `__class__`指向创建，`__bases__`指向继承。

这种关系是由于类的继承的，类的继承有：

- 单一继承
- 多重继承
- 菱形继承（钻石继承）
- 继承机制 MRO
- MRO 的C3 算法

菱形继承的问题，如果N父类中有相同的方法，继承哪个？

深度优先：父类查找，再去父父类找。。。

属于经典类的查找方式，新式类的查找方式属于广度优先。如果一个父类中没有，再去另一个父类中找，最后再去父父类中找。

##### 多重继承的顺序问题

可以用 `SubClass.mro()`来理清这个过程。

手动理清的话，需要用到有向无环图：DAG(Directed Acyclic Graph)

- DAG 原本是一种数据结构，因为DAG的拓扑结构带来的优异特性，经常被用于处理动态规划、寻找最短路径的场景。
- DAG中有入度为0的点，没有谁去依赖它
- 查找都是从左侧开始，入度为0 的先查找

##### 重载

python 中没有实现重载，按代码顺序执行。

#### 9、solid 设计原则与设计模式&单例模式

设计模式的指导原则 SOLID设计原则：

- 单一责任原则 The Single Responsibility Principle
  - 一个类只能有一个被修改的理由
  - 比如一个爬虫类，网站改版，并且需要改输出模式，2件事情，需要把类拆开
  - 违反这个原则，改功能的时候，可能会对另外的功能产生影响。
  - 类承担的职责越多，复杂度也越高，维护起来也更麻烦。
  - 爬取网站、逻辑处理、存储文件都需要单独存类。确保单独的类单独的功能。
- 开放封闭原则 The Open Closed Principle
  - 对类的扩展是开放的，对修改是封闭的
  - 如果需要扩展一部分功能，不应该去修改类的代码，而是在外面增加 `classmethod`
- 里氏替换原则 THe Liskov Substitution Principle
  - 继承中，子类实现的功能要完整的覆盖到父类的方法，这么做的好处是不用管是父类实例化的，还是子类实例化的。
- 依赖倒置原则 The Dependency Inversion Principle
  - 高层的模块不应该以来低层模块
  - 需要的话做抽象处理
- 接口分离原则 The Interface Segregation Principle
  - 接口隔离原则
  - 接口是模块之间相互交流的协议
  - 接口与需求要匹配

后面2个原则多用于静态语言，和 python 关系不大。

##### 单例模式

程序在实例化的时候只允许出现一个实例。

对象只存在一个实例。

`__init__`和 `__new__`的区别：

- `__new__`是实例创建之前被调用，返回该实例对象，是**静态方法**，是真正的构造函数。
- `__init__` 是实例对象创建完成后被调用，是**实例方法**
- `__new__` 先被调用， `__init__`后被调用
- `__new__`的返回值（实例）将传递给 `__init__`方法的第一个参数，  `__init__`个这个实例设置相关参数

单例模式需要注意，如果是多线程创建实例，需要去做加锁操作。

#### 10、工厂模式

简单的工厂模式可以对自己的程序解耦。

动态的工厂模式可以动态的创建类，和后面的元类有关系。

想去实现工厂模式需要包含三种角色：

- 工厂角色：负责产生实例，判断输入参数
- 抽象产品角色，角色的父类，提供公共接口
- 产品角色，不同的属性，根据传入参数不同，实现不同的名字

##### 类工厂模式

在函数内动态创建的类

```python
def factory3(func):
    class klass:pass
    setattr(klass,func.__name__,classmethod(func))
    return klass
def say_bar(cls):
    print('bar')
    print(cls)
    
f = factory3(say_bar)
f.say_bar()
```

#### 11、元类

工厂模式比较复杂，不够灵活。

python 中用元类的方式创建比较轻松。

创建类的类，就是元类，是类的模板。可以用 type 和 class 创建。

**一般是写框架的时候用到的，平时写程序很少用到**。

元类是用来控制如何创建类的，正如类是创建对象的模板一样。控制类在刚开始创建的时候它应该有什么样的动作。

元类的实例为类，正如类的实例为对象。

- 元类必须继承自 `type`
- 元类必须实现 `__new__`方法

#### 12、Mixin模式

抽象基类，派生出的子类如果没有全部实现父类的方法，会报错，而不是让子类继续运行。用来确保派生类实现了基类中的特定方法。

好处：

- 避免继承错误，使类层次易于理解和维护。
  - 父类中去定义抽象基类，不用对父类再去进行一些类的实例化
- 无法实例化基类
- 如果忘记在其中一个子类中实现接口方法，要尽早报错

##### Mixin模式

在程序运行过程中，重定义类的继承，即动态继承。好处：

- 可以在不修改任何源代码的情况下，对已有类进行扩展
- 进行组件的划分

```python
# 整体结构如下
# def mixin 将类加在一起，实现动态继承
# 注意用 mrc 理清继承顺序
def mixin(Klass,MixinKlass):
    Klass.__bases__ = (MixinKlass,) + Klass.__bases__
    
class Fclass(object):
    def text(self):
        print('in FatherClass')
        
class S1class(Fclass):
    pass
class MixinClass(object):
    def text(self):
        print('in MixinClass')
        return super().text() #加载父类功能
        
        
class S2class(S1class,MixinClass):
    pass
print(f'test1: S1class MRO: {S1class.mro()}')


mixin(S1class,MixinClass)
print(f'test1: S1class MRO: {S1class.mro()}')
s1 = S1class()
s1.text()
```

> 需要注意的是：`MixinClass` 中的 `super()`并不指向 `MixinClass`的父类，而是 另有所指。
>
> 也就是说 `super()` 并不一定指向当前类的父类，而是要看 `mro()`的继承顺序。

```python
class Displayer():
    def display(self, message):
        print(message)

class LoggerMixin():
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super(LoggerMixin, self).display(message)
        self.log(message)

class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')

subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")
print(MySubClass.mro())

# 输出
‘’‘
This string will be shown and logged in subclasslog.txt
[<class '__main__.MySubClass'>, <class '__main__.LoggerMixin'>, <class '__main__.Displayer'>, <class 'object'>]
’‘’
```

> `super(LoggerMixin, self).display(message)`
>
> 将引用关系进入 `Displayer`中
>
> 所以`super（`）指向的是 `mro` 顺序中的后一个