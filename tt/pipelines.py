# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tt.DatabaseHandler import DatabaseHandler


class TtPipeline(object):
    def __init__(self):
        self.db = DatabaseHandler(host="0.0.0.0", username="root", password="mysql", database="pc")

    def close_spider(self,spider):
        self.db.close()

    def process_item(self, item, spider):
        sql = "insert into sohu(title,href) values('%s','%s');"%(item['title'],item['href'])
        self.db.insert(sql)
        return item
