# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy 
#scrapy下载图片用的模块
from scrapy.pipelines.images import ImagesPipeline 
from scrapy.exceptions import DropItem

class ImgPipeline(ImagesPipeline):
    #抓取图片url获取request用于下载
    def get_media_requests(self,item,info):
        yield scrapy.Request(item['imageUrl'])

    #请求得到后执行该方法
    def item_completed(self,results,item,info):
        image_path=[x['path'] for ok,x in results if ok]

        #判断是否成功
        if not image_path:
            raise DropItem('没图片')
        else:
            print 'success'
        item['image_path']=image_path
        return item
