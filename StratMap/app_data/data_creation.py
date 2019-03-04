
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
    data = {'hospital_types': [{'1': 'ללים'}, {'2': 'גריאטריים'}, {'3': 'פסיכיאטריים'}]}
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
    d = {'measure': [{'id': i['_id']['$oid'], 'measure_name': i['measure_name']} for i in l]}
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
    v.del_all('app_data_version')


def test_vers_update():
    v = DataBase()
    v.connect()
    data = {
        'active': False,
        'measure': [
            {'id': '5c3f057d326f4218684a8f28', 'measure_name': 'מבחן'},
            {'id': '5c3efdaf326f4218684a8f24', 'measure_name': 'מדד השני'}
        ],
        'version_desc': '',
        'version_name': 'גרסה ב',
        'version_type': '1',
        'version_number': '1001',
        'hospital_type': '1'
    }

    v.post('app_data_version', data)