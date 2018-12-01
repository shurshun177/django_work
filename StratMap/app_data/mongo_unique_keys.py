import pymongo
myclient = pymongo.MongoClient("mongodb://192.168.34.6:27017/")


def vers_unique():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_version"]
    mycol.create_index([
        ('hospital_type', pymongo.ASCENDING),
        ('version_number', pymongo.DESCENDING)
    ], unique=True)


def meas_unique():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_measure"]
    mycol.create_index([
        ('measure_code', pymongo.DESCENDING),
        ('hospital_type', pymongo.ASCENDING)
    ], unique=True)


def acttual_unique():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_measure"]
    mycol.create_index([
        ('measure_code', pymongo.DESCENDING),
        ('hospital_type', pymongo.ASCENDING),
        ('version_number', pymongo.DESCENDING),
        ('hospital_code', pymongo.ASCENDING)
    ], unique=True)


meas_unique()
