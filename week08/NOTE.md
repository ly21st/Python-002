# 学习笔记


# 变量赋值

# collections 
collections 官方文档：
https://docs.python.org/zh-cn/3.7/library/collections.html

# 使用collections扩展内置数据类型
![52e953870cf261ff89eff28e2a7ee59d.png](en-resource://database/14522:1)

```
    
    # 命名元组
    from collections import namedtuple
    Point = namedtuple('Ponit', ['x','y'])
    p = Point(10, y=20)
    p.x + p.y
    p[0] + p[1]
    x, y = p
    from collections import Counter
    mystring = ['a','b','c','d','d','d','d','c','c','e']
    # 取得频率最高的前三个值
    cnt = Counter(mystring)
    cnt.most_common(3)
    cnt['b']
    # 双向队列
    from collections import deque
    d = deque('uvw')
    d.append('xyz')
    d.appendleft('rst')

```

# namedtuple的例子与魔术方法
```
    
    import numpy as np
    '''
    计算欧式距离
    '''
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])
    op1 = np.sqrt(np.sum(np.square(vector1-vector2)))
    op2 = np.linalg.norm(vector1-vector2)
    from collections import namedtuple
    from math import sqrt
    Point = namedtuple('Ponit', ['x','y','z'])
    class Vector(Point):
        def __init__(self, p1, p2, p3):
            super(Vector).__init__()
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3

        def __sub__(self, other):
            tmp = (self.p1 - other.p1)**2+(self.p2 - other.p2)**2+(self.p3 - other.p3)**2
            return sqrt(tmp)
    p1 = Vector(1, 2, 3)
    p2 = Vector(4, 5, 6)
    print(p1-p2)


```

# 魔术方法__call___
```
        In [1]: class Kls1(object):
       ...:     def __call__(self):
       ...:         return 123
       ...:

    In [2]: inst1=Kls1()

    In [3]: inst1
    Out[3]: <__main__.Kls1 at 0x221a832bd08>

    In [4]: inst1()
    Out[4]: 123

    In [5]:
```

# 变量作用域
切换分支：git checkout 6b

# 6. 函数工具与高阶函数

```
    
    def func(*args, **kargs):
        print(f'args: {args}')
        print(f'kargs:{kargs}')
    func(123, 'xz', name='xvalue')

```

## lambda表达式
![8dd3055bbe755959d4cfc3e63b477c3e.png](en-resource://database/14942:0)


## 高阶函数
![8e6171be85f45317bf28d5851ab26811.png](en-resource://database/14944:0)

```
    
# map
def square(x):
    return x**2
m = map(square, range(10))
next(m)
list(m)
[square(x) for x in range(10)]
dir(m)


# filter
def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))



import functools
add_1 = functools.partial(add, 1)
add_1(10)
import itertools
g = itertools.count()
next(g)
next(g)
auto_add_1 = functools.partial(next, g)
auto_add_1()


sorted(['bob', 'about', 'Zoo', 'Credit'])
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


```

#  闭包
## 返回值
![7e07532e75c47984a381334fb05a0c1c.png](en-resource://database/14946:0)

```
    
    # version 1
    # 函数是一个对象，所以可以作为某个函数的返回结果
    def line_conf():
        def line(x):
            return 2*x+1
        return line       # return a function object
    my_line = line_conf()
    print(my_line(5))


```

## 输出闭包的局部变量和自由变量
```
    
    def line_conf():
        b = 10
        def line(x):
            '''如果line()的定义中引用了外部的变量'''
            return 2*x+b
        return line       
    b = -1
    my_line = line_conf()
    print(my_line(5))
    # 编译后函数体保存的局部变量
    print(my_line.__code__.co_varnames)
    print("------------------------")
    # 编译后函数体保存的自由变量
    print(my_line.__code__.co_freevars)
    print("--------------------")
    # 自由变量真正的值
    print(my_line.__closure__[0].cell_contents)


```

## 内部函数对外部函数变量的引用
```
    
# 内部函数对外部函数作用域里变量的引用（非全局变量）则称内部函数为闭包
    def counter(start=0):
       count=[start]
       def incr():
           count[0]+=1
           return count[0]
       return incr
    c1=counter(10)
    print(c1())
    # 结果：11
    print(c1())
    # 结果：12
    # nonlocal访问外部函数的局部变量
    # 注意start的位置，return的作用域和函数内的作用域不同
    def counter2(start=0):
        def incr():
            nonlocal start
            start+=1
            return start
        return incr
    c1=counter2(5)
    print(c1())
    print(c1())
    c2=counter2(50)
    print(c2())
    print(c2())
    print(c1())
    print(c1())
    print(c2())
    print(c2())
    print("------------")
    def counter3(start=0):
        result = start
        def incr():
        #    nonlocal result
            result = result + 1
            return result
        return incr
    c3=counter3(5)
    print(c3())


```

# 装饰器
```
    
    # 装饰器, @ 语法糖
    @decorate   
    def func2():
        print('do sth')
    # 等效于下面
    def func2():
        print('do sth')
    func2 = decorate(func2)

```

## 装饰器使用例子
```
    
    # 装饰器在模块导入的时候自动运行
    # testmodule.py
    def decorate(func):
        print('running in modlue')
        def inner():
            return func()
        return inner
    @decorate
    def func2():
        pass

```

## 装饰器例子2
```
    
    # 包装
    def html(func):
        def decorator():
            return f'<html>{func()}</html>'
        return decorator
    def body(func):
        def decorator():
            return f'<body>{func()}</body>'
        return decorator
    @html
    @body
    def content():
        return 'hello world'
    content()

```

## 带参数的装饰器
```
    
    # 被修饰函数带参数
    def outer(func):
        def inner(a,b):
            print(f'inner: {func.__name__}')
            print(a,b)
            func(a,b)
        return inner
    @outer
    def foo(a,b):
        print(a+b)
        print(f'foo: {foo.__name__}')


    foo(1,2)
    foo.__name__

```

## 带不定长参数的装饰器
```
    
    def outer2(func):
        def inner2(*args,**kwargs):
            func(*args,**kwargs)
        return inner2
    @outer2
    def foo2(a,b,c):
        print(a+b+c)

    foo2(1,3,5)


```
## 带返回值的装饰器
```
    
    # 被修饰函数带返回值
    def outer3(func):
        def inner3(*args,**kwargs):
            ###
            ret = func(*args,**kwargs)
            ###
            return ret
        return inner3
    @outer3
    def foo3(a,b,c):
        return (a+b+c)

    print(foo3(1,3,5))


```

# python内置装饰器
```
    
    from time import ctime,sleep
    from functools import wraps
    def outer_arg(bar):
        def outer(func):
            # 结构不变增加wraps
            @wraps(func)
            def inner(*args,**kwargs):
                print("%s called at %s"%(func.__name__,ctime()))
                ret = func(*args,**kwargs)
                print(bar)
                return ret
            return inner
        return outer
    @outer_arg('foo_arg')
    def foo(a,b,c):
        """  __doc__  """
        return (a+b+c)

    print(foo.__name__)


```

## function tools缓存
```
    
    import functools
    @functools.lru_cache()
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-2) + fibonacci(n-1)
    if __name__=='__main__':
        import timeit
        print(timeit.timeit("fibonacci(6)", setup="from __main__ import fibonacci"))


```

# 类装饰器
```
    
    from functools import wraps
    class MyClass(object):
        def __init__(self, var='init_var', *args, **kwargs):
            self._v = var
            super(MyClass, self).__init__(*args, **kwargs)

        def __call__(self, func):
            # 类的函数装饰器
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                func_name = func.__name__ + " was called"
                print(func_name)
                return func(*args, **kwargs)
            return wrapped_function
    def myfunc():
        pass
        
        
    MyClass(100)(myfunc)()

```

## 装饰类
```
    
    # 装饰类
    def decorator(aClass):
        class newClass(object):
            def __init__(self, args):
                self.times = 0
                self.wrapped = aClass(args)

            def display(self):
                # 将runtimes()替换为display()
                self.times += 1
                print("run times", self.times)
                self.wrapped.display()
        return newClass
    @decorator
    class MyClass(object):
        def __init__(self, number):
            self.number = number
        # 重写display
        def display(self):
            print("number is",self.number)
    six = MyClass(6)
    for i in range(5):
        six.display()

```

# 对象协议
![b3a87cf6825e471ab150f2bfbecb1468.png](en-resource://database/14948:0)

# 格式化字符串
```
    
    import math
    print('The value of Pi is approximately %5.3f.' % math.pi)
    print('{1} and {0}'.format('spam', 'eggs'))
    print('The story of {0}, {1}, and {other}.'.format(
        'Bill', 'Manfred', other='Georg'))
    firstname = 'yin'
    lastname = 'wilson'
    print('Hello, %s %s.' % (lastname, firstname))
    print('Hello, {1} {0}.'.format(firstname, lastname))
    print(f'Hello, {lastname} {firstname}.')
    f'{ 2 * 5 }'
    class Person:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
        def __str__(self):
            return f'hello, {self.first_name} {self.last_name}.'
        def __repr__(self):
            return f'hello, {self.first_name} {self.last_name}.'
    me = Person('yin', 'wilson')
    print(f'{me}')


```

# 生成器
![bb0ebbc4f87fa23267437a244a947dff.png](en-resource://database/14950:0)
![087d890ccf9d7e1cead5bd62e404ebbd.png](en-resource://database/14952:0)

![35d2a7eb5af2d25f8d23a4dd38243450.png](en-resource://database/14954:0)

# 协程与线程的区别
![2859858a5c9639f2d9b80b11a74b109b.png](en-resource://database/14956:0)

# 异步编程
![4fc0d32a24eba04d57b247608ce025d5.png](en-resource://database/14958:0)
