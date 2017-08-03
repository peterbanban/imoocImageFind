# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class Imagepipeline(object):

    def open_spider(self,spider):
        self.file=open('jsonImage.json','w')

    def process_item(self, item, spider):
        buf=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(buf)
        return item
    
    def close_spider(self,spider):
        self.file.close()
