from pymongo import MongoClient
from bson.objectid import ObjectId
import re

class DataBase:

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

    '''
     method get_all() takes tuple of document`s fields that we
     need or don`t need (depends on include arguments, that`s
     equal to False by default) to get from the collection and
     dictionary of fields that uses for filter results.
     Returns query-object.
    '''


    def find(self, col, filter={}, fields=None):

        query = self.db[col].find(filter=filter, projection=fields)
        return query

    def update_doc(self, id, **kwargs):
        query = {'id': id}
        new_values = {'$set': kwargs}
        #self.collection.update_one(query, new_values)

    def get_by_id(self, collection, id):
        query = dict()
        query['_id'] = ObjectId(id)
        res = self.db[collection].find(query)
        return res

    def is_valid_id(self, _id):
        return  (isinstance(_id, str) and re.match("[\d\w]{24}", _id)) or isinstance(_id, ObjectId)




if __name__ == '__main__':



    test_vers = {
        'version_number': 1000,
        'hospital_type': '1',
        'version_name': 'גרסה ינואר-אפריל 2018',
        'version_type': '1',
        'version_desc': 'test',
        'active': True,
        'measure_id': [],
        'cancel': False,
        'create_user': 'artur',
        'change_date': None,
        'change_user': '',
        'cancel_date': None,
        'cancel_user': ''
    }
    #a = v.collection.insert_one(test_vers)
    #v = DataBase()
    #v.connect()
    #print([i for i in v.get_by_id('app_data_measure', '5bffc610326f4225e4ff69f9')])




