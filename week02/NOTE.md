# 学习笔记

# 异常捕获与处理资料

1. 获取课程源码操作方法：
git checkout 2d
2. pretty_errors 官方文档链接：
https://pypi.org/project/pretty-errors/
3. try 语句官方文档：
https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-try-statement
4. with 语句官方文档：
https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-with-statement
5. with 语句上下文管理器官方文档：
https://docs.python.org/zh-cn/3.7/reference/datamodel.html#with-statement-context-managers

# 自定义异常

```
    
    class UserInputError(Exception):
        def __init__(self, ErrorInfo):
            super().__init__(self, ErrorInfo)
            self.errorinfo = ErrorInfo
        def __str__(self):
            return self.errorinfo

    userinput = 'a'
    try:
        if (not userinput.isdigit()):
            raise UserInputError('用户输入错误')
    except UserInputError as ue:
        print(ue)
    finally:
        del userinput

```


# 美化异常输出
```
    
    import pretty_errors
    
    def foo():
        1/0
    foo()
```

# 打开文件
```
    
    file1 = open('a.txt', encoding='utf8')
    try:
        data = file1.read()
    finally:
        file1.close()
    with open('a.txt', encoding='utf8') as file2:
        data = file2.read()


```

# 自定义with open
```
    
    class Open:
        def __enter__(self):
            print("open")
        def __exit__(self, type, value, trace):
            print("close")

        def __call__(self):
            pass
    with Open() as f:
        pass
    # 上下文协议

```

# 使用PyMySQL进行数据库操作
1. 获取课程源码操作方法：
git checkout 2d
2. MySQL 官方文档手册：
https://dev.mysql.com/doc/
3. MySQL 官方下载连接：
https://dev.mysql.com/downloads/mysql/
4. PyMySQL 官方文档:
https://pypi.org/project/PyMySQL/


# mysql设置字符集
```
    [client]
    #default-character-set=utf8
    default-character-set=utf8mb4

    [mysql]
    #default-character-set=utf8
    default-character-set=utf8mb4

    [mysqld]
    character-set-client-handshake = FALSE
    collation-server = utf8mb4_unicode_ci 
    #collation-server = utf8_unicode_ci
    #init-connect='SET NAMES utf8'
    init-connect='SET NAMES utf8mb4'
    #character-set-server = utf8
    character-set-server = utf8mb4
    wait_timeout=31536000
    interactive_timeout=31536000
```

```
    [client]
    default-character-set=utf8mb4

    [mysql]
    default-character-set=utf8mb4

    [mysqld]
    character-set-client-handshake = FALSE
    collation-server = utf8mb4_unicode_ci
    init-connect='SET NAMES utf8mb4'
    character-set-server = utf8mb4
    wait_timeout=31536000
    interactive_timeout=31536000

```

# 分布式爬虫

![d5fd5798ad7fedb3bc58909bb23fdeae.png](en-resource://database/6251:1)

# user agent
关键头部： user agent, refer, host

# 5. 反爬虫：使用WebDriver模拟浏览器行为

1. 获取课程源码操作方法：
切换分支：git checkout 2e

2. WebDriver 文档：

  https://www.w3.org/TR/webdriver/
  https://www.selenium.dev/selenium/docs/api/py/
3. ChromeDriver 下载地址：
  https://chromedriver.storage.googleapis.com/index.html


# 6. 反爬虫：验证码识别

1. 获取课程源码操作方法：
切换分支：git checkout 2e
2. 各种语言识别库：
https://github.com/tesseract-ocr/tessdata

# 7. 爬虫中间件&系统代理IP

执行  # scrapy crawl httpbin 或 # scrapy crawl httpbin --nolog  

# 8. 自定义中间件&随机代理IP

1. 获取课程源码操作方法：
切换分支：git checkout 3a
2. 补充说明：
6 分 55 秒处，setting.py 配置项说明：

用大写是一种约定行为，scrapy 自带的设置都是大写，如果要修改默认的配置项，那必须是大写（因为 scrapy 内部对这些配置的处理都是大写的）。
如果是自定义的中间件或扩展和配置项，自己是可以控制配置项是否是大小写的，但建议使用者尽量遵守约定，使用全大写。


# 下载中间件
![d60f8e4b08bbf367a0c6601c2ae2b023.png](en-resource://database/6255:1)


# redis查看分布式爬虫结果
![9765ec8db5b95bdf98aedbb6ed815d42.png](en-resource://database/6260:1)

# 9. 分布式爬虫

1. 获取课程源码操作方法：
切换分支：git checkout 3b
2. redis 官方网址：
https://redis.io/


# mysql连接例子
![b851ad32dc1c9170dec7e042c0505c7e.png](en-resource://database/6286:0)

