from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo import ReturnDocument
import re
import datetime

from bson.json_util import dumps


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

    def update(self, col, data, id):
        query = {'_id': ObjectId(id)}
        data = {'$set': data}
        return self.db[col].find_one_and_update(filter=query, update=data,
                                                        return_document=ReturnDocument.AFTER)

    def get_by_id(self, collection, id):

        query = dict()

        query['_id'] = ObjectId(id)
        res = self.db[collection].find(query)
        return res

    def post(self, collection, data):  # data is dict
        res = self.db[collection].insert_one(data)
        return res.inserted_id

    def is_valid_id(self, _id):
        return  (isinstance(_id, str) and re.match("[\d\w]{24}", _id)) or isinstance(_id, ObjectId)

    def delete(self, collection, id):
        data = {'_id': ObjectId(id)}
        query =  self.db[collection].delete_one(data)






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
    def up():
        v = DataBase()
        v.connect()
        d = datetime.datetime.utcnow()
        data = {'cancel': True, 'cancel_user': 'CAeldon', 'cancel_date': d}
        v.update('app_data_measure', data, '5bffc61a326f421b74873460')

    def fin():
        v = DataBase()
        v.connect()
        k = v.find('app_data_measure', filter={'cancel_date': None}, fields={'cancel_date': 1})
        print([i for i in k])

    def del_test(col, list_id):
        v = DataBase()
        v.connect()
        for i in list_id:
            v.delete(col, i)

    def del_measure_false():
        v = DataBase()
        v.connect()
        data = {}
        data['cancel'] = False
        list_id = ['5bffc72c326f4227047ed645', '5bffc61a326f421b74873460', '5bffc610326f4225e4ff69f9']
        for i in list_id:
            query = v.update('app_data_measure', data, i)
            if query is None:
                print('Operation was refused')


    def del_vers_false():
        v = DataBase()
        v.connect()
        data = {}
        data['cancel'] = False
        list_id = ['5bffc72c326f4227047ed645', '5bffc61a326f421b74873460', '5bffc610326f4225e4ff69f9']
        for i in list_id:
            query = v.update('app_data_version', data, i)
            if query is None:
                print('Operation was refused')


    del_test('app_data_measure', ['5c07fcd8326f4209fcbcda32', '5c07fd12326f4209fcbcda33', '5c07fd9e326f42393c2a13a8'])


