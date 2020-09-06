# 学习笔记



# 三种方法
![1a03063a67d332b689b313289ad88892.png](en-resource://database/6984:1)

# 类方法
```
    
    class Book(object):
        def __init__(self, title):
            self.title = title
        @classmethod
        def create(cls, title):
            book = cls(title=title)
            return book
    book1 = Book("python")
    book2 = Book.create("python and django")
    print(book1.title)
    print(book2.title)

```

# 静态方法
```
    
    class Book(object):
        def __init__(self, title):
            self.title = title
        @classmethod
        def create(cls, title):
            book = cls(title=title)
            return book
    book1 = Book("python")
    book2 = Book.create("python and django")
    print(book1.title)
    print(book2.title)


```

# 属性的处理
![7517e74dcc63aa369948ee88f8962f5b.png](en-resource://database/6986:1)

# object与type的关系
![83be54174fa1dae36addffbd3d495e7f.png](en-resource://database/6988:1)

# 多重继承的顺序问题
![d1eb2310c41613ca1ec07a1ca22a1f13.png](en-resource://database/6990:1)

用mro()方法或者有向无环图（从左到右分析）
```
    
    # 钻石继承
    class BaseClass(object):
        num_base_calls = 0
        def __init__(self):
            print('in BaseClass __init__')
        def call_me(self):
            print ("Calling method on Base Class")
            self.num_base_calls += 1
    class LeftSubclass(BaseClass):
        num_left_calls = 0
        def __init__(self):
            super().__init__()
            print('in LeftSubclass __init__')
        def call_me(self):
            print ("Calling method on Left Subclass")
            self.num_left_calls += 1
    class RightSubclass(object):
        num_right_calls = 0
        def __init__(self):
            super().__init__()
            print('in RightSubclass __init__')
        def call_me(self):
            print("Calling method on Right Subclass")
            self.num_right_calls += 1
    class Subclass(LeftSubclass,RightSubclass):
        def __init__(self):
            super().__init__()
            print('in Subclass __init__')
        pass
    a = Subclass()
    a.call_me()
    print(Subclass.mro())

```


# SOLID设计原则
![e95951ad9fb212ec7e399ba02c5083b0.png](en-resource://database/7010:1)

# 单例模式
![99f9d7ff0ea2254512626d7d1471f225.png](en-resource://database/7012:1)

# 元类
![82872397a87a49ef6a6ae4f2796b874c.png](en-resource://database/7014:0)

```
    
    # 使用type元类创建类
    def hi():
        print('Hi metaclass')
    # type的三个参数:类名、父类的元组、类的成员
    Foo = type('Foo',(),{'say_hi':hi})
    foo = Foo
    foo.say_hi()
    # 元类type首先是一个类，所以比类工厂的方法更灵活多变，可以自由创建子类来扩展元类的能力
    def pop_value(self,dict_value):
        for key in self.keys():
            if self.__getitem__(key) == dict_value:
                self.pop(key)
                break
    # 元类要求,必须继承自type    
    class DelValue(type):
        # 元类要求，必须实现new方法
        def __new__(cls,name,bases,attrs):
            attrs['pop_value'] = pop_value
            return type.__new__(cls,name,bases,attrs)

    class DelDictValue(dict,metaclass=DelValue):
        # python2的用法，在python3不支持
        # __metaclass__ = DelValue
        pass
    d = DelDictValue()
    d['a']='A'
    d['b']='B'
    d['c']='C'
    d.pop_value('C')
    for k,v in d.items():
        print(k,v)
 

```

# 抽象基类
![f13dd07dcd471fa4fd07cce78fba8bfe.png](en-resource://database/7016:0)


```
    
    from abc import ABCMeta, abstractmethod
    class Base(metaclass=ABCMeta):
        @abstractmethod
        def foo(self):
            pass
        @abstractmethod
        def bar(self):
            pass
    class Concrete(Base):
        def foo(self):
            pass
    c = Concrete() # TypeError


```

# MiXin模式

![2b1cc619659aec801f4fdcb52a57e9d5.png](en-resource://database/7018:0)

## 动态修改父类
```
    
    def mixin(Klass, MixinKlass):
        Klass.__bases__ = (MixinKlass,) + Klass.__bases__
    class Fclass(object):
        def text(self):
            print('in FatherClass')
    class S1class(Fclass):
        pass
    class MixinClass(object):
        def text(self):
            # return super().text()
            print('in MixinClass')
    class S2class(S1class, MixinClass):
        pass
    print(f' test1 : S1class MRO : {S1class.mro()}')
    s1 = S1class()
    s1.text()
    mixin(S1class, MixinClass)
    print(f' test2 : S1class MRO : {S1class.mro()}')
    s1 = S1class()
    s1.text()
    print(f' test3 : S2class MRO : {S2class.mro()}')
    s2 = S2class()
    s2.text()


```

# 获取属性顺序
__getattribute__ >__getattr__ > __dict__ 这是读取一个属性时的默认顺序