from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from bson.objectid import ObjectId
from pymongo import ReturnDocument
import re
import datetime
from settings import DATABASES


class NationalData:

    db_host = DATABASES['default']['HOST']
    db_port = DATABASES['default']['PORT']
    name = DATABASES['default']['NAME']
    def __init__(self):
        self.host = '{}:{}'.format(self.db_host, self.db_port)
        self.db_name = self.name
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

    def update(self, col, data, id=None, req=None):
        if id and self.is_valid_id(id):
            query = {'_id': ObjectId(id)}
        else:
            query = req
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

    def del_all(self, col, query={}):
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

    def append(self, col, filter, field_name, value, id=None, req=None):
        if id:
            query = {'_id': ObjectId(id)}
        else:
            query = req
        data = {'$push': {field_name: value}}
        return self.db[col].find_one_and_update(filter=query, update=data,
                                                        return_document=ReturnDocument.AFTER)


    def search(self, col, search_field, text):
        text = '.*{}.*'.format(text)
        query = self.db[col].find({search_field: {'$regex': text}}, filter={'cancel': 'false'})
        return query





def postData():
    v = NationalData()
    v.connect()
    data = {'measure_code': '978.01.90',
            'year': '2019',
            'hospital_type': '1',
            'actual_value': [
                {
                    'entry_seq': '0',
                    'entry_value': '1529',
                    'create_data': '03.02.2019',
                    'change_date': ''
                },
                {
                    'entry_seq': '1',
                    'entry_value': '1944',
                    'create_data': '03.02.2019',
                    'change_date': ''
                },
            ]}
    v.post('app_data_nationalaverage', data=data)

def get_data():
    v = NationalData()
    v.connect()
    filt = {
        'year': {'$in':[
            '2019','2017'
        ]
        },
        'hospital_type': '1'
    }

    l = [i for i in v.find('app_data_nationalaverage', filt)]
    l_new = [i.get('actual_value') for i in l]
    for i in l:
        print(i)

def del_wrong(col):
    v = NationalData()
    v.connect()
    data = {'year': '2018'}
    v.delete(col, del_query=data)

def up(d):
    v = NationalData()
    v.connect()
    data = {
        'actual_value': [
            {
                'entry_seq': '0',
                'national_measure': d.get('national_measure'),
                'create_data': '03.02.2019',
                'change_date': ''
            },
            {
                'entry_seq': '1',
                'average_measure': d.get('average_measure'),
                'create_data': '03.02.2019',
                'change_date': ''
            },
        ]
    }
    krit = {
        'measure_code': '978.01.90',
        'hospital_type': '2',
        'year': '2018'
    }
    v.update('app_data_nationalaverage', data=data, req=krit)

def up_test(d):
    v = NationalData()
    v.connect()
    current_date = datetime.datetime.utcnow()
    actual_value = [
            {
                'entry_seq': '1',
                'app_data_nationalaverage': d.get('average_measure'),
                'create_data': current_date,
                'change_date': ''
            }
        ]



    data = {'actual_value.1.entry_valu': d.get('average_measure'), 'actual_value.0.entry_value': d.get('national_measure')}
    krit = {
        'measure_code': '17.19.23',
        'hospital_type': '1',
        'year': '2018'
    }
    v.update('app_data_nationalaverage', data=data, req=krit)

def get_business():
    v = NationalData()
    v.connect()
    filt = {
        # 'name': 'business_topic',

    }

    l = [i for i in v.find('app_data_decryptiontables', filt, {'values_list': 1})]
    l_new = [i.get('actual_value') for i in l]
    for i in l:
        print(i)

def get_meas(hosp, y1, y2):
    v = NationalData()
    v.connect()
    filt = {
        'year': {'$in': [
            y1, y2
        ]
        },
        'hospital_type': hosp
    }
    query = [i for i in v.find('app_data_measure', fields={'measure_code': 1, 'measure_name': 1})]
    for i in query:
        print(i)
    l = [i for i in v.find('app_data_nationalaverage', filt)]
    for i in l:
        print(i)

    for j in l:
        for i in query:
            if i.get('measure_code') == j.get('measure_code'):
                print(i.get('measure_code'), j.get('measure_code'), j.get('actual_value'))
                i[j.get('year')] = j.setdefault('actual_value')


    for i in query:
        print('2018: {}   2019: {}'.format(i.get('2018'), i.get('2019')))

    print(query)

def up_business():
    v = NationalData()
    v.connect()
    data = {
        'values_list.2': [
            {'code': '3',
             'name': 'חווית המטופל',
             'sub_topic': [{'code': '31', 'name': 'מלר"ד'},
                           {'code': '32', 'name': 'זימון וניהול תור'},
                           {'code': '33',
                            'name': 'ביצוע סקרי שביעות רצון'},
                           {'code': '34', 'name': 'אשפוז באגף הפנימי'}]
             }
        ],
    }
    krit = {
        'name': 'business_topic'
    }
    v.update('app_data_decryptiontables', data=data, req=krit)

def get_hosp():
    v = NationalData()
    v.connect()
    data = {
        'values_list.type': 1
    }
    query = v.find('app_data_decryptiontables', {'name': 'hospital_codes', 'values_list.type': '1'}, fields=data)
    for i in query: print(i)

def getCells(year, hosp, meas_code):
    v = NationalData()
    v.connect()
    filt = {
        'year': year,
        'hospital_type': hosp,
        'measure_code': meas_code
    }

    l = [i for i in v.find('app_data_nationalaverage', filt, {'actual_value': 1})]
    l_new = [i.get('actual_value') for i in l]
    for i in l:
        print(i)

def modify(d):
    v = NationalData()
    v.connect()

    current_date = datetime.datetime.utcnow()
    krit = {
        'measure_code': d.get('measure_code'),
        'hospital_type': d.get('hospital_type'),
        'year': d.get('year')
    }
    l = v.exists('app_data_nationalaverage', krit)

    if l == 0:
        data = {'measure_code': d.get('measure_code'),
                'year': d.get('year'),
                'hospital_type': d.get('hospital_type'),
                'actual_value': [
                    {
                        'national_measure': d.get('national_measure'),
                        'create_data': current_date,
                        'create_user': '',
                        'change_date': '',
                        'change_user': ''
                    },
                    {
                        'average_measure': d.get('average_measure'),
                        'create_data': current_date,
                        'create_user': '',
                        'change_date': '',
                        'change_user': ''
                    },
                ]}
        try:
            v.post('app_data_nationalaverage', data=data)
        except:
            return {'status': 'not created'}
        return {'status': 'created'}
    else:
        if d.get('national_measure') and d.get('average_measure'):
            data = {'actual_value.0.national_measure': d.get('national_measure'),
                    'actual_value.0.change_date': current_date,
                    'actual_value.1.average_measure': d.get('average_measure'),
                    'actual_value.1.change_date': current_date,
                    }
            try:
                v.update('app_data_nationalaverage', data=data, req=krit)
            except:
                return {'status': 'failed'}
            return {'status': 'updated'}
        elif d.get('national_measure'):
            data = {'actual_value.0.national_measure': d.get('national_measure'),
                    'actual_value.0.change_date': current_date
                    }
            try:
                v.update('app_data_nationalaverage', data=data, req=krit)
            except:
                return {'status': 'failed'}
            return {'status': 'updated'}
        elif d.get('average_measure'):
            data = {'actual_value.1.average_measure': d.get('average_measure'),
                    'actual_value.1.change_date': current_date,
                    }
            try:
                v.update('app_data_nationalaverage', data=data, req=krit)
            except:
                return {'status': 'failed'}
            return {'status': 'updated'}

def division(hosp, topic):
    v = NationalData()
    v.connect()
    col = 'app_data_measure'

    filter = {
        'hospital_type': hosp,
        'business_topic': topic,
        'active': True,
        'is_division': True,
        'cancel': False
    }
    fields = {
        'measure_name': 1,
        'measure_code': 1,
        'is_division': 1
    }
    measures = [i for i in v.find(col, filter, fields)]
    print(measures)

# del_wrong('app_data_nationalaverage')
# get_data()
# postData()
# up({'national_measure': '123', 'average_measure': '196'})
# up_test({'average_measure': '18826', 'national_measure': '33982'})
# get_business()
# get_meas('1', '2018', '2019')
# up_business()
# get_hosp()
# getCells('2018', '2', '978.01.90')
# modify({'year': '2018', 'hospital_type': '1', 'measure_code': '366.63.53', 'national_measure': '484'})
# division('2', '1')