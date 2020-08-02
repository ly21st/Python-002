# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
import pymysql
import traceback


DB_INFO = {
    'host': '10.8.4.121',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'maoyan'
}


class DbConnObj(object):
    def __init__(self, db_info):
        self.host = db_info['host']
        self.port = db_info['port']
        self.user = db_info['user']
        self.password = db_info['password']
        self.db = db_info['db']
        self.init()

    def __del__(self):
        self.close()

    def init(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        self.create_table('movie')

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute(self, stmt, args=None):
        cur = self.conn.cursor()

        try:
            cur.execute(stmt, args)
            # print('after execute,result:', cur.fetchone())
            cur.close()
            self.conn.commit()
        except Exception as e:
            print(traceback.format_exc())
            print('execute {}, args={} error.'.format(stmt, args))
            if cur:
                cur.close()
            self.conn.rollback()

    def create_table(self, tb_name):
        self.execute('DROP TABLE IF EXISTS `%s`' % (tb_name))
        sql = '''create table `%s`(
                    id int(4) primary key not null auto_increment,
                    title varchar(32),
                    film_type varchar(64),
                    film_date varchar(32)
                )'''
        self.execute(sql % (tb_name))


dbConnObj = DbConnObj(DB_INFO)


class MaoyanmoviePipeline:
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        if not item:
            return
        title = item['title']
        film_type = item['film_type']
        film_date = item['film_date']
        dbConnObj.execute(
            'insert into movie(`title`, `film_type`, `film_date`) values("%s", "%s", "%s")' % (title, film_type, film_date))
