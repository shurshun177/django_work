from django.test import TestCase

import requests
import json
def req_vers_id(id):
    url = 'http://127.0.0.1:8000/api/v0/versions/{}/'.format(id)
    r = requests.get(url)
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def req_vers():
    url = 'http://127.0.0.1:8000/api/v0/versions/'
    r = requests.get(url)
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def req_measures():
    url = 'http://127.0.0.1:8000/api/v0/measures/'
    r = requests.get(url)
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def req_get_measure(id):
    url = 'http://127.0.0.1:8000/api/v0/measures/{}/'.format(id)
    r = requests.get(url)
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def del_vers(id):
    url = 'http://127.0.0.1:8000/api/v0/version/del_vers/{}/'.format(id)
    r = requests.put(url)
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def del_measure(id):
    url = 'http://127.0.0.1:8000/api/v0/measure/del_measure/{}/'.format(id)
    r = requests.put(url)
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def orm():
    url = 'http://127.0.0.1:8000/api/v1.0/post/'
    r = requests.get(url)
    print(r.status_code, r.content)


def put_vers(id):
    url = 'http://127.0.0.1:8000/api/v0/version/update/{}/'.format(id)
    data = {
        'version_number': 1002,
        'hospital_type': '1',
        'create_date': '2018, 11, 28, 0, 0',
        'version_name': 'גרסה ינואר-םפטמבר 2016',
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
    r = requests.put(url, json.dumps(data))
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def post_vers():
    data = {
        'version_number': 1004,
        'hospital_type': '1',
        'version_name': 'גרסה ינואר-םפטמבר 2016',
        'version_type': '1',
        'version_desc': 'test',
        'active': True,
        'measure_id': []
    }
    url = 'http://127.0.0.1:8000/api/v0/versions/'
    r = requests.post(url, json.dumps(data))
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def post_measures():
    data = {
        'active': True,
        'business_topic': '2',
        'criteria_inclusion': '',
        'denominator': '',
        'digit_num': None,
        'from_date': None,
        'hospital_type': '1',
        'measure_code': '6.04.07',
        'measure_desc': '',
        'measure_name': 'שיעור תפוסה לפי תקן מיטות',
        'measure_type': '',
        'measure_unit': None,
        'measuring_frequency': '1',
        'numerator': '',
        'remarks': '',
        'removal_criteria': '',
        'separate_thousands': None,
        'target_default': 100.0,
        'to_date': None
    }
    url = 'http://127.0.0.1:8000/api/v0/measures/'
    r = requests.post(url, json.dumps(data))
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def main():
    req_vers()
    req_vers_id('5c06741b326f423a3830e55f') # right id
    req_vers_id('5bffc626326f4227d0bcffd7') # wrong id
    req_measures()
    req_get_measure('5bffc626326f4227d0bcffd7') # right id
    req_get_measure('5c06741b326f423a3830e55f') # wrong id
    available()


def req_index_0():
    data = {
        'version_number': 1005,
        'hospital_type': '3',
        'version_name': 'גרסה ינואר-םפטמבר 2016',
        'version_type': '1',
        'version_desc': 'test',
        'active': True,
        'measure_id': []
    }
    url = 'http://127.0.0.1:8000/api/v0/test/'
    r = requests.post(url, json.dumps(data))
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def put_measure(id):
    url = 'http://127.0.0.1:8000/api/v0/measure/update/{}/'.format(id)
    data = {
        'active': True,
        'business_topic': 'פעילות',
        'criteria_inclusion': '',
        'denominator': '',
        'digit_num': None,
        'from_date': None,
        'hospital_type': '1',
        'measure_code': '1.03.00',
        'measure_desc': 'Figniya',
        'measure_name': 'צריכת חשמל ומים',
        'measure_type': 'ON TARGET',
        'measure_unit': None,
        'measuring_frequency': '1',
        'numerator': '',
        'remarks': '',
        'removal_criteria': '',
        'separate_thousands': None,
        'target_default': 100.0,
        'to_date': None
    }
    r = requests.put(url, json.dumps(data))
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json())
    else:
        print(r.status_code, r.text)


def available():
    url = 'http://127.0.0.1:8000/api/v0/available_measures/'
    r = requests.put(url)
    if r.headers['Content-Type'] == 'application/json':
        print(r.status_code, r.json(), r.headers)
    else:
        print(r.status_code, r.text)

#req_index_0()
#del_measure('5bffc72c326f4227047ed645')
#req_measures()
#put_measure('5bffc626326f4227d0bcffd5')
#req_get_measure('5c064999326f4218c899310f')
#put_vers('5bffba4b326f4239a4d20554')
#del_vers('5c056048326f422e603957d1')
#post_vers()
#req_measures()
#del_vers('5c056048326f422e603957d1')
#req_vers_id('5c06424d326f422acc020bde')
#post_measures()
#available()
#req_get_measure('5c065d97326f423a3830e55e')
req_measures()
available()
req_vers()
