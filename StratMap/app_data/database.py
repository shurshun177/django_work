from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from bson.objectid import ObjectId
from pymongo import ReturnDocument
import re
import datetime



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


    def find(self, col, filter={}, fields=None, skip=0, limit=1000):

        query = self.db[col].find(filter=filter, projection=fields, skip=skip, limit=limit)
        return query

    def get(self, col, sorted_by=None, ascending=True, fields=None, skip=0, limit=1000):
        query = {}
        sort = None
        if sorted_by:
            if ascending:
                sort = [(sorted_by, ASCENDING)]
            else:
                sort = [(sorted_by, DESCENDING)]
        res = self.db[col].find(filter=query, sort=sort, projection=fields, skip=skip, limit=limit)
        return res

    def update(self, col, data, id):
        if id and self.is_valid_id(id):
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

    def post_many(self, collection, data_list):  # list of dicts
        res = self.db[collection].insert_many(data_list)
        return res

    def is_valid_id(self, _id):
        return  (isinstance(_id, str) and re.match("[\d\w]{24}", _id)) or isinstance(_id, ObjectId)

    def delete(self, collection, del_query, id=None):
        if id:
            data = {'_id': ObjectId(id)}
        else:
            data = del_query
        query = self.db[collection].delete_one(data)
        return query

    def cancel_false(self, col, query, data):
        data = {'$set': data}
        return self.db[col].find_one_and_update(filter=query, update=data,
                                                return_document=ReturnDocument.AFTER)

    def exists(self, col, query={}):
        return self.db[col].count(filter=query)

    def del_all(self, col, query):
        return self.db[col].delete_many(query)

    def add_to_set(self, col, filter, field_name, value):
        if isinstance(value, list):
            data = {'$addToSet': {field_name: {'$each': value}}} # if more then one value,
        else:                                                   # must use list
            data = {'$addToSet': {field_name: value}}         # data = [{'code': '1', 'type': 'חטיבה'}]
                # v.add_to_set('app_data_decryptiontables', {'name': 'hospital_codes'}, 'values_list', data)
        return self.db[col].find_one_and_update(filter=filter,
                                                        update=data,
                                                        return_document=ReturnDocument.AFTER)


    def search(self, col, search_field, text):
        text = '.*{}.*'.format(text)
        query = self.db[col].find({search_field: {'$regex': text}})
        return query


if __name__ == '__main__':


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


    def canc_false(col):
        v = DataBase()
        v.connect()
        number_of_doc = v.exists(col, {'cancel': True})
        for i in range(number_of_doc):
            v.cancel_false(col, {'cancel': True}, data={'cancel': False, 'cancel_user': '', 'cancel_date': ''})

    def number_cancel(col):
        v = DataBase()
        v.connect()
        number_of_doc = v.exists(col, {'cancel': True})
        print(number_of_doc)



    def del_dup():
        v = DataBase()
        v.connect()
        print(v.is_connected())
        v.del_all('app_data_version', {'version_name': ''})
        v.del_all('app_data_measure', {'measure_name': ''})


    def dec_tab(name):
        from collections import Iterable
        v = DataBase()
        v.connect()
        val = None
        try:
            k = v.find('app_data_decryptiontables', filter={'name': name})
            val = k[0]['values_list']
        except:
            print('Database exeption')
        return val

    def post_test():
        v = DataBase()
        v.connect()
        data = {'hospital_types': [{'1': 'ללים'}, {'2': 'גריאטריים'} , {'3': 'פסיכיאטריים'}]}
        k = v.post('app_data_decryptiontables', data)


    def new_test():
        v = DataBase()
        v.connect()
        v.get('app_data_version', id='5c164722326f423ce4c54b55')

    def test_get():
        v = DataBase()
        v.connect()
        k = v.get('app_data_version', sorted_by='create_date', ascending=False, fields={'version_number'}, limit=1)
        val = [i.get('version_number') for i in k][0]
        if not isinstance(val, int):
            res = int(val) + 1
        else:
            res = val + 1
        print(res)

    def test_measures():
        l = [{'_id': {'$oid': '5c079152326f421a04aa7bce'}, 'measure_name': 'שיעור תפוסה לפי תקן מיטות'},
              {'_id': {'$oid': '5c079152326f421a04aa7bce'}, 'measure_name': 'שיעור תפוסה לפי תקן מיטות'}]
        d = {'measure':[{'id': i['_id']['$oid'], 'measure_name': i['measure_name']} for i in l]}
        print(d)
        v = DataBase()
        v.connect()
        print(v.is_connected())
        v.post('app_data_version', d)

    def testSearch(text):
        v = DataBase()
        v.connect()
        print(v.is_connected())
        for i in v.search('app_data_version', 'version_name', text):
            print(i)

    def delCodes():
        v = DataBase()
        v.connect()
        v.del_all('app_data_decryptiontables', {'name': 'business_topic'})


    def create_hosp_codes():
        v = DataBase()
        v.connect()
        values_list = [{'hosp_code': '01103', 'name': 'ביה"ח אסף הרופה', 'type': '1'},
                       {'hosp_code': '01108', 'name': 'ביה"ח ברזילי', 'type': '1'},
                       {'hosp_code': '01204', 'name': 'ביה"ח בני ציון', 'type': '1'},
                       {'hosp_code': '01107', 'name': 'ביה"ח נהריה', 'type': '1'},
                       {'hosp_code': '01106', 'name': 'ביה"ח הלל יפה', 'type': '1'},
                       {'hosp_code': '01109', 'name': 'ביה"ח פוריה', 'type': '1'},
                       {'hosp_code': '01102', 'name': 'ביה"ח רמבם', 'type': '1'},
                       {'hosp_code': '01201', 'name': 'ביה"ח איכילוב', 'type': '1'},
                       {'hosp_code': '01104', 'name': 'ביה"ח וולפסון', 'type': '1'},
                       {'hosp_code': '01105', 'name': 'ביה"ח זיו', 'type': '1'},
                       {'hosp_code': '01101', 'name': 'ביה"ח שיבה', 'type': '1'},
                       {'hosp_code': '11101', 'name': 'ביה"ח שער המנשה', 'type': '3'},
                       {'hosp_code': '11102', 'name': 'ביה"ח יהודה אברבנאל', 'type': '3'},
                       {'hosp_code': '11103', 'name': 'ביה"ח ע"ש פליגלמן מזור', 'type': '3'},
                       {'hosp_code': '11104', 'name': 'המרכז לבריאות הנפש בער יעקב', 'type': '3'},
                       {'hosp_code': '11105', 'name': 'המרכז הרפואי לברה''נ לב השרון', 'type': '3'},
                       {'hosp_code': '11106', 'name': 'ביה"ח מעלה הכרמל', 'type': '3'},
                       {'hosp_code': '11107', 'name': 'המרכז לבריאות הנפש בער שבה', 'type': '3'},
                       {'hosp_code': '11109', 'name': 'מרכז רפואי לבריאות הנפש ירושלים', 'type': '3'},
                       {'hosp_code': '21101', 'name': 'מרכז רפואי גריאטרי שמואל הרופא', 'type': '2'},
                       {'hosp_code': '21102', 'name': 'מרכז גריאטרי שיקומי ע''ש פלימן', 'type': '2'},
                       {'hosp_code': '22101', 'name': 'מרכז הגריאטרי המשולב ע"ש שוהם', 'type': '2'},
                       {'hosp_code': '22102', 'name': 'מרכז גריאטרי דורות נתניה', 'type': '2'},
                       {'hosp_code': '22103', 'name': 'מרכז גריאטרי ראשל"צ', 'type': '2'},
                       {'hosp_code': '31101', 'name': 'מרכז קהילתי לבריאות הנפש', 'type': '2'},
                       {'hosp_code': '1', 'name': 'חטיבה', 'type': '0'}]
        data = {'name': 'hospital_codes', 'values_list': values_list}
        v.post('app_data_decryptiontables', data)

    #new_test()
    # canc_false('app_data_version')
    # number_cancel('app_data_version')
    # del_test('app_data_decryptiontables', ['5c122e78326f422f60f66b1d'])
    # canc_false('app_data_measure')
    # del_dup()
    # test_get()
    # test_measures()
    # print(try_to_add())
    # create_hosp_codes()
    # delCodes()
    # post_test()