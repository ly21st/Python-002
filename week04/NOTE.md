
# 1. pandas简介

说明：19 分 54 秒处的 df[1:3] 应该是 df[0:3] ，这里的原理和 Python 数组的切片是一样的。

1. 获取课程源码操作方法：
切换分支：git checkout 4a
2. pandas 中文文档：
https://www.pypandas.cn/
sklearn-pandas
3. 安装参考文档：
https://pypi.org/project/sklearn-pandas/1.5.0/
4. Numpy 学习文档：
https://numpy.org/doc/
5. matplotlib 学习文档：
https://matplotlib.org/contents.html

# pandas读
```
    
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    import os
    pwd = os.path.dirname(os.path.realpath(__file__))
    book = os.path.join(pwd,'book_utf8.csv')
    # df = pd.read_csv('book_utf8.csv')
    df = pd.read_csv(book)
    # 输出全部内容
    print(df)

```
默认读取，第一行数据会当成标题
```

    >>> df['还行']
    0      较差
    1      还行
    2      力荐
    3      还行
    4      很差
           ..
    575    较差
    576    还行
    577    力荐
    578    推荐
    579    力荐
    Name: 还行, Length: 580, dtype: object
```

# 数据聚合与增加列
```

    # 数据聚合，数字才聚合，忽略文字
    df.groupby('star').sum()
    # 创建新列
    star_to_number = {
        '力荐' : 5,
        '推荐' : 4,
        '还行' : 3,
        '较差' : 2,
        '很差' : 1
    }
    df['new_star'] = df['star'].map(star_to_number)
    print(df)

```

# Series
```

    >>> emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
    >>> emails
    0    abc at amazom.com
    1       admin1@163.com
    2             mat@m.at
    3           ab@abc.com
    dtype: object
    >>>
    >>>
    >>>
    >>> import re
    >>> pattern ='[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'
    >>> mask = emails.map(lambda x: bool(re.match(pattern, x)))
    >>> mask
    0    False
    1     True
    2     True
    3     True
    dtype: bool
    >>> emails
    0    abc at amazom.com
    1       admin1@163.com
    2             mat@m.at
    3           ab@abc.com
    dtype: object
    >>> emails[mask]
    1    admin1@163.com
    2          mat@m.at
    3        ab@abc.com
    dtype: object
    >>>
```

# 读取数据库
```
    imoprt pymysql
    sql  =  'SELECT *  FROM users'
    conn  = conn = pymysql.connect('10.8.4.121','root','123456','db',charset='utf8')
    df = pd.read_sql(sql,conn)
    
    >>> df
    id                   email       password
    0   1    webmaster@python.org    very-secret
    1   2    webmaster@python.org    very-secret
    2   3  'webmaster@python.org'  'very-secret'
    3   4    webmaster@python.org    very-secret
    4   5    webmaster@python.org    very-secret
    >>>
```

# series
Series 学习文档：https://pandas.pydata.org/pandas-docs/stable/reference/series.html

# DataFrame
DataFrame 学习文档：https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

# pandas计算功能
Pandas 计算功能操作文档：https://pandas.pydata.org/docs/user_guide/computation.html#method-summary

# mysql多表连接
MySQL 数据库多表连接学习文档：https://dev.mysql.com/doc/refman/8.0/en/join.html

# pandas输出和绘图
2. plot 学习文档：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
3. seaborn 学习文档：http://seaborn.pydata.org/tutorial.html

#  jieba分词与提取关键词

2. jieba 学习文档：https://github.com/fxsjy/jieba/blob/master/README.md

# SnowNLP情感倾向分析
snowNLP 参考学习地址：https://github.com/isnowfy/snownlp/blob/master/README.md
