from __future__ import unicode_literals
from pymongo import MongoClient
from pymongo import ReturnDocument
from pymongo import ASCENDING, DESCENDING
from bson.objectid import ObjectId
from bson.json_util import dumps
import re
import datetime


class MongoDBManager:
    def __init__(self):
        self.host = '192.168.34.6:27017'
        self.db_name = 'StrategicMap'
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(self.host)
        self.db = self.client[self.db_name]

    def is_connected(self):
        return self.db is not None

    def post(self, object_name, data):  # data is dict
        if '_id' in data.keys():
            data.pop('_id')
        res = self.db[object_name].insert_one(data)
        return res

    def post_many(self, object_name, data_list):  # list of dicts
        res = self.db[object_name].insert_many(data_list)
        return res

    def get(self, object_name, id=None, sorted_by=None, ascending=True, fields=None, skip=0, limit=1000):
        query = dict()
        sort = None
        if sorted_by:
            if ascending:
                sort = [(sorted_by, ASCENDING)]
            else:
                sort = [(sorted_by, DESCENDING)]
        if id and self.is_valid_id(id):
            query['_id'] = ObjectId(id)
            return self.db[object_name].find_one(filter=query, sort=sort)

        return [o for o in
                self.db[object_name].find(filter=query, sort=sort, projection=fields, skip=skip, limit=limit)]

    def find_one(self, object_name, filter, fields=None):
        return self.db[object_name].find_one(filter=filter, projection=fields)

    def find(self, object_name, filter, fields=None, skip=0, limit=1000):
        return self.db[object_name].find(filter=filter, projection=fields, skip=skip, limit=limit)

    def is_valid_id(self, _id):
        return  (isinstance(_id, str) and re.match("[\d\w]{24}", _id)) or isinstance(_id, ObjectId)

    def update(self, object_name, data, id):
        query = {'_id': ObjectId(id)}
        data = {'$set': data}
        return self.db[object_name].find_one_and_update(filter=query, update=data,
                                                        return_document=ReturnDocument.AFTER)

    def increase_value(self, object_name, id, field_name, value):
        query = {'_id': ObjectId(id)}
        data = {'$inc': {field_name: value}}
        return self.db[object_name].find_one_and_update(filter=query, update=data,
                                                        return_document=ReturnDocument.AFTER)

    def delete(self, object_name, id):
        query = {'_id': ObjectId(id)}
        return self.db[object_name].delete_one(query)

    def append(self, object_name, id, field_name, value):
        query = {'_id': ObjectId(id)}
        data = {'$push': {field_name: value}}
        return self.db[object_name].find_one_and_update(filter=query, update=data,
                                                        return_document=ReturnDocument.AFTER)

    def add_to_set(self, object_name, id, field_name, value):
        query = {'_id': ObjectId(id)}
        if isinstance(value, list):
            data = {'$addToSet': {field_name: {'$each': value}}}
        else:
            data = {'addToSet': {field_name: value}}
        return self.db[object_name].find_one_and_update(filter=query,
                                                        update=data,
                                                        return_document=ReturnDocument.AFTER)

    def remove(self, object_name, id, field_name, child_id=None, value=None):
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
        query = {'_id': id}
        data = None
        if child_id:
            data = {'$pull': {field_name: {"_id": child_id}}}
        elif value:
            data = {'$pull': {field_name: value}}
        if data:
            return self.db[object_name].find_one_and_update(filter=query, update=data,
                                                            return_document=ReturnDocument.AFTER)

    def complex_update(self, object_name, filter, update):
        return self.db[object_name].find_one_and_update(filter=filter, update=update,
                                                        return_document=ReturnDocument.AFTER)

    def exists(self, object_name, id):
        query = {'_id': ObjectId(id)}
        return self.db[object_name].count(filter=query) > 0

    def aggregate(self, object_name, pipeline, ):
        return self.db[object_name].aggregate(pipeline)


if __name__ == '__main__':
    pass