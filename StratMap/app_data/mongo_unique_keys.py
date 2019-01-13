import pymongo
myclient = pymongo.MongoClient("mongodb://192.168.34.6:27017/")


def vers_unique():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_version"]
    mycol.create_index([
        ('version_number', pymongo.DESCENDING)
    ], unique=True)


def meas_unique():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_measure"]
    mycol.create_index([
        ('measure_code', pymongo.DESCENDING)
    ], unique=True)


def actual_unique():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_actualexecution"]
    mycol.create_index([
        ('measure_code', pymongo.DESCENDING),
        ('version_number', pymongo.DESCENDING),
        ('hospital_code', pymongo.ASCENDING)
    ], unique=True)

def search_vers():
    mydb = myclient["StrategicMap"] # search field have to be index
    mycol = mydb["app_data_version"]
    mycol.create_index([('version_name', 'text')])

def search_measure():
    mydb = myclient["StrategicMap"]  # search field have to be index
    mycol = mydb["app_data_measure"]
    mycol.create_index([('measure_desc', 'text')])

# search_measure()

