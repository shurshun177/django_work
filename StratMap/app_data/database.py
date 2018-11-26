import pymongo


class DataBase:
    '''
    class DataBase takes database`s IP adress and name
    and implements method get_all(), that allows get
    data from collection.
    '''
    url = "mongodb://192.168.34.6:27017/"
    client = pymongo.MongoClient(url)
    name_db = "StrategicMap"
    mydb = client[name_db]

    def __init__(self, collection):
        self.collection = self.mydb[collection]

    '''
     method get_all() takes tuple of document`s fields that we
     need or don`t need (depends on include arguments, that`s
     equal to False by default) to get from the collection and
     dictionary of fields that uses for filter results.
     Returns query-object.
    '''


    def get_all(self, *filds, **filt):
        hide_fields = {i: 0 for i in filds}
        hide_fields['_id'] = 0
        query = self.collection.find(filt, hide_fields)
        return query

    #def update_doc(self,):


if __name__ == '__main__':
    v = DataBase("app_data_version")


    test_vers = {
        'version_number': 1003,
        'hospital_type': '1',
        'version_name': 'test_vers',
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
    k = [i for i in v.collection.find()]
    print(k)




