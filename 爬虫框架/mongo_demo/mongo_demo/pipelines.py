# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import pymysql


class MongoPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.douban.movie.insert_one(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class MysqlPipeline:
    def open_spider(self, spider):
        self.client = pymysql.connect(host='localhost', port=3306, user='root', password='123', db='douban',
                                      charset='utf8')
        self.cursor = self.client.cursor()

    def process_item(self, item, spider):
        args = [item['name'], item['star']]
        sql = 'insert into t_movie VALUES (0,%s,%s)'
        self.cursor.execute(sql, args)
        self.client.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.client.close()
