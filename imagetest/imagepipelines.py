# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy 
#scrapy����ͼƬ�õ�ģ��
from scrapy.pipelines.images import ImagesPipeline 
from scrapy.exceptions import DropItem

class ImgPipeline(ImagesPipeline):
    #ץȡͼƬurl��ȡrequest��������
    def get_media_requests(self,item,info):
        yield scrapy.Request(item['imageUrl'])

    #����õ���ִ�и÷���
    def item_completed(self,results,item,info):
        image_path=[x['path'] for ok,x in results if ok]

        #�ж��Ƿ�ɹ�
        if not image_path:
            raise DropItem('ûͼƬ')
        else:
            print 'success'
        item['image_path']=image_path
        return item