import redis
import json
import pymongo
redis_client = redis.Redis(host='localhost', port=6379, db=0)
mongo_client = pymongo.MongoClient()
collection = mongo_client.room.lianjia
while True:
    key, data = redis_client.blpop(['lianjia:items'])
    print(key)
    d = json.loads(data)
    collection.insert(d)
