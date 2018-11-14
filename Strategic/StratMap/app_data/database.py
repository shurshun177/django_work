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


    def get_all(self, *filds, **filter):
        hide_fields = {i: 0 for i in filds}
        query = self.collection.find(filter, hide_fields)
        return query


if __name__ == '__main__':
    v1 = DataBase("app_data_version")
    values_list = [i for i in v1.get_all('_id', 'cancel', version_number=1000)]
    print(values_list)


