import pymongo
from app_data.settings import DATABASES
import app_data.create_values

db_name = DATABASES['default']['NAME']
db_host = DATABASES['default']['HOST']
db_port = DATABASES['default']['PORT']
db_url = 'mongodb://{}:{}/'.format(db_host, db_port)
myclient = pymongo.MongoClient(db_url)



def vers_unique():
    mydb = myclient[db_name]
    mycol = mydb["app_data_version"]
    mycol.create_index([
        ('version_number', pymongo.DESCENDING)
    ], unique=True)


def meas_unique():
    mydb = myclient[db_name]
    mycol = mydb["app_data_measure"]
    mycol.create_index([
        ('measure_code', pymongo.DESCENDING)
    ], unique=True)


def actual_unique():
    mydb = myclient[db_name]
    mycol = mydb["app_data_actualexecution"]
    mycol.create_index([
        ('measure_code', pymongo.DESCENDING),
        ('version_number', pymongo.DESCENDING),
        ('hospital_code', pymongo.ASCENDING)
    ], unique=True)


def national_average_unique():
    mydb = myclient[db_name]
    mycol = mydb["app_data_nationalaverage"]
    mycol.create_index([
        ('measure_code', pymongo.DESCENDING),
        ('hospital_type', pymongo.DESCENDING),
        ('year', pymongo.ASCENDING)
        ],
        unique=True
    )




if __name__ == '__main__':
    print(db_name, db_host, db_port, db_url, sep='\n')
    # vers_unique()
    # meas_unique()
    # actual_unique()
    # national_average_unique()


