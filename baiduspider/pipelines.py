# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from baiduspider.settings import MONGODB_DBNAME, MONGODB_HOST,MONGODB_PORT,MONGODB_SHEETNAME
from baiduspider import items
import pymongo


class BaiduspiderPipeline(object):
    def __init__(self):

        host = MONGODB_HOST
        port = MONGODB_PORT
        dbname = MONGODB_DBNAME
        sheetname = MONGODB_SHEETNAME

        client = pymongo.MongoClient(host = host,port=port)
        mydb = client[dbname]
        self.mysheet = mydb[sheetname]

    def process_item(self,item,spider):
        if isinstance(item, items.QuestionItem):
            data = dict(item)
            self.mysheet.insert({"_id":data['questionNum'],"question":data['question'],
                                 "questionDes":data['questionDes'],"questionUrl":data['questionUrl']})


        if isinstance(item, items.OtheransItem):
            data = dict(item)
            self.mysheet.update_one({"_id": item['questionNum']}, {"$set": {("%s.%s") % (item['questionNum'], int(item['rate']*100)):
                {
                    "otherAns":data['otherAns'],
                    "otherPostime":data['otherPostime'],
                    "otherUp":data['otherUp'],
                    "otherDown":data['otherDown'],
                    "otherAuthor":data['otherAuthor'],
                    "rate":data['rate']


                    }}}, True)

        if isinstance(item, items.BestansItem):
            data = dict(item)
            self.mysheet.update_one({"_id": item['questionNum']}, {"$set": {("%s.%s") % (item['questionNum'], int(item['rate']*100)):
                {
                    "bestAns": data['bestAns'],
                    "bestPostime": data['bestPostime'],
                    "bestUp": data['bestUp'],
                    "bestDown": data['bestDown'],
                    "bestAuthor": data['bestAuthor'],
                    "rate": data['rate']

                }
                    }}, True)

        return item