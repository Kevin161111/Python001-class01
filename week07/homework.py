
""" 
1.定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。
2.动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
3.猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
4.动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。

"""
from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self,animal_type,body_shape,character):
        self.animal_type = animal_type
        self.shape = body_shape
        self.character = character
        
    @property
    def is_fierce(self):
        if self.shape != "小" and self.animal_type == "食肉" and self.character== '凶猛':
            return True
        return False
   
   # get self.shape
    @property
    def shape(self):
        return self._shape 
    
    # set self.shape
    @shape.setter
    def shape(self,body_shape):
        if body_shape not in ['大','中','小']:
            raise Exception("请输入正确的体型：['大','中','小']")
        self._shape = body_shape

class Cat(Animal):

    voice = "喵喵喵"

    def __init__(self,name,animal_type,shape,character):
        super(Cat,self).__init__(animal_type,shape,character)
        self.name = name

    @property
    def is_good_as_pet(self):
        if self.is_fierce:
            return False
        return True

class Zoo:

    def __init__(self,name):
        self.name = name
        self.animals = []

    def add_animal(self,animal_type):
        if type(animal_type).__name__ in self.animals:
            print(f'{type(animal_type).__name__} existed in {self.name}')
        else:
            self.animals.append(type(animal_type).__name__)
            self.__dict__[type(animal_type).__name__] = animal_type

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    print(cat1.name)
    print(cat1.animal_type)
    print(cat1.shape)
    print(cat1.character)
    print(cat1.voice)
    print(cat1.is_good_as_pet)
    # 测试 cat2
    cat2 = Cat('大花猫 2', '食肉', '大', '凶猛')
    print(cat2.shape)
    print(f'is {cat2.name} is fierce?' , cat2.is_fierce)
    print(  f"is {cat2.name} good as pet?" ,cat2.is_good_as_pet)

    # 增加一只猫到动物园
    z.add_animal(cat1)
    #-----测试多一只效果
    z.add_animal(cat2)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(z.animals)
    a = Animal()
    print(a)
