# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import json

#BACKEND_URL = 'http://localhost:8080/'
BACKEND_URL = 'https://requestbin.fullcontact.com/1ius7l61?inspect'


class RecordReleaseWaterPipeline(object):
    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if hasattr(spider, 'backendUrl'):
            url = spider.backendUrl + '/api'
        else:
            url = BACKEND_URL + "/aip"
        headers = {'content-type': 'application/json'}
        itemDict = dict(item)
        payload = {}
        payload['releaseDate'] = itemDict['releaseDate']
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        return item