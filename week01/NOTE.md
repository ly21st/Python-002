# 学习笔记



# 学习资料

requests 官方文档链接： https://requests.readthedocs.io/zh_CN/latest/

获取课程源码操作方法

git clone https://github.com/wilsonyin123/geekbangtrain.git

cd geekbangtrain

git checkout 1a

注：如果 GitHub 网页加载过慢，可以使用 https://gitee.com/wilsonyin/pythontrain.git 代替:

git clone https://gitee.com/wilsonyin/pythontrain.git

cd pythontrain

git checkout 1a

# 需求分析

豆瓣电影网站  
https://movie.douban.com/top250

# 代码


# xpath插件


# 使用BeautifulSoup
按F2，选择Elements标签，点击指针按钮，然后点击页面上的电影名称，可以看到电脑名称对应的源代码的位置，然后通过python代码实现。
```

    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a'):
            print(atag.get('href'))
            # 获取所有链接
            # print(atag.find('span').text)
            # 获取电影名字
            for span in atag.find_all('span'):
                print(span.text)

```

find_all方法找所有元素，find方法找一个元素。


# Beautiful Soup 官方文档链接 
https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

# xpath使用
选择代码，右键-》copy xpath，
然后ctrl+f，再粘贴选中的内容。


# python 基础语法

Python 简介： https://docs.python.org/zh-cn/3.7/tutorial/introduction.html

Python 数据结构： https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html

Python 其他流程控制工具 : https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html

Python 中的类： https://docs.python.org/zh-cn/3.7/tutorial/classes.html

Python 定义函数： https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html#defining-functions

# python的关键字


# 推导式写法


# html基础


W3C 标准官方文档：https://www.w3.org/standards/

# http状态码


	
	| http状态码 |  |
	| --- | --- |
	|1xx  |信息响应  |
	|2XX  |成功响应 |
	|3XX  |重定向  |
	|4XX  |客户端响应  |
	|5XX  |服务端响应  |



# Scrapy 架构官方文档介绍：

https://docs.scrapy.org/en/latest/topics/architecture.html


# scrapy核心组件


# scrapy架构


# scrapy安装位置及结构


# 运行scrapy

 scrapy crawl douban

# xpath详解

1. 获取课程源码操作方法
切换分支：git checkout 2c
2. Scrapy Xpath 官方学习文档： https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths
3. Xpath 中文文档：
https://www.w3school.com.cn/xpath/index.asp
4. Xpath 英文文档：
https://www.w3.org/TR/2017/REC-xpath-31-20170321/#nt-bnf

5. 补充说明：
* 12 分 32 秒处“打印的选择器信息用 元祖 括起来”，此处有一点小的问题，相信细心的同学已经察觉到了，注意我们需把 元祖 改成 列表。

* 18 分 18 秒处视频中讲述 “ dont_filter 设置为 True 后，不会受到 allowed_domains 的限制”。更正为 dont_filter 设置为 True，是用来解除去重功能。Scrapy 自带 url 去重功能，第二次请求之前会将已发送的请求自动进行过滤处理。所以将 dont_filter 设置为 True 起到的作用是解除去重功能，一旦设置成重 True，将不会去重，直接发送请求。

# yield与推导式

1. 获取课程源码操作方法
切换分支：git checkout 2d
2. yield 表达式官方文档：
https://docs.python.org/zh-cn/3.7/reference/expressions.html#yieldexpr
3. yield 语句官方文档
https://docs.python.org/zh-cn/3.7/reference/simple_stmts.html#yield
4. Python 推导式官方文档：
https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html#list-comprehensions
5. 补充说明：
视频中老师所讲 yield 返回的是单独的一个值，更准确的说返回的值必须是对象，在此章节我们暂定只把它理解返回一个值。在后面的章节多线程部分，我们会结合课程再对 yield 进行详解。

# yield语句

```

    def chain(num):
        for it in range(num):
            yield it
    num = 5 
    y = chain(num)
    next(y)
    list(y)
```

# 爬虫小结

* 获取网页内容requests.get方法
* 解析网页，提取内容，用BeautifulSoup或者用lxml.etree.HTML取得selector对象，
然后用selector.xpath
* 使用scrapy爬虫框架，框架中解析内容可以用BeautifulSoup也可以通过
from scrapy.selector import Selector
然后使用Selector(response.text).xpath进行解析。
* xpath比BeautifulSoup方法方便很多，效率也高很多。
* 通过yield返回比return返回解析后的内容好，return一次性返回所有数据，yield一次只返回一次数据，避免内存消耗过多的情况。
* 习惯列表推导式，而不是使用显示循环，代码更加python化。
* 掌握基础前端调试方式，xpath表达式。





