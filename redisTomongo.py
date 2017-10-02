# coding:utf-8
import pymongo
import json
import redis

def redis_tomongo():
    rediscli = redis.Redis(host="127.0.0.1", port=6379, db=0)
    host = "127.0.0.1"
    port = 27017
    dbname = "baidu"
    sheetname = "zhidao"
    client = pymongo.MongoClient(host=host, port=port)
    mydb = client[dbname]
    mysheet = mydb[sheetname]
    num=0
    while True:
        try:
            source, data = rediscli.blpop("zhidaospider:items")
            item = json.loads(data)
            if item.has_key('question'):
                mysheet.insert({"_id": item['questionNum'], "question": item['question'],
                                     "questionDes": item['questionDes'], "questionUrl": item['questionUrl']})
                num +=1
                print num

            elif item.has_key('otherPostime'):
                mysheet.update_one({"_id": item['questionNum']},{"$set": {("%s.%s") % (item['questionNum'], int(item['rate'] * 100)):
                                    {
                                        "otherAns": item['otherAns'],
                                        "otherPostime": item['otherPostime'],
                                        "otherUp": item['otherUp'],
                                        "otherDown": item['otherDown'],
                                        "otherAuthor": item['otherAuthor'],
                                        "rate": item['rate']
                                    }
                                }}, True)
                num +=1
                print num
            else:
                mysheet.update_one({"_id": item['questionNum']},{"$set": {("%s.%s") % (item['questionNum'], int(item['rate'] * 100)):
                                       {
                                           "bestAns": item['bestAns'],
                                           "bestPostime": item['bestPostime'],
                                           "bestUp": item['bestUp'],
                                           "bestDown": item['bestDown'],
                                           "bestAuthor": item['bestAuthor'],
                                           "rate": item['rate']

                                       }
                                   }}, True)
                num+=1
                print num
        except Exception,e:
            print e

if __name__=="__main__":
    redis_tomongo()
