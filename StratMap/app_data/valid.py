from datetime import datetime as d
def is_valid_code(measure_code):
    t = '0123456789.'
    test_func = map(lambda x: x in t, measure_code)
    c = False not in list(test_func)
    return c



def is_valid_measure(data):
    fields = (
        'measure_code',
        'measure_name',
        'measure_desc',
        'hospital_type',
        'measure_type',
        'measure_unit',
        'business_topic',
        'digit_num'
    )
    for i in fields:
        if not data.get(i) or data.get(i) == '0':
            return False
    return True


def is_valid_update_measure(data):
    fields = (
        'measure_name',
        'measure_desc',
        'measure_type',
        'measure_unit',
        'business_topic',
        'digit_num'
    )
    for i in fields:
        if not data.get(i) or data.get(i) == '0':
            return False
    return True


def is_valid_version(data):
    fields = (
        'version_number',
        'version_name',
        'version_type',
        'hospital_type'
        # additional field measure
    )
    for i in fields:
        if not data.get(i) or data.get(i) == '0':
            return False
    return True


def is_valid_update_version(data):
    fields = (
        'version_name',
        'version_type',
        # additional field measure
    )
    for i in fields:
        if not data.get(i) or data.get(i) == '0':
            return False
    return True


d = {'version_number': '1004',
     'version_name': 'דצמבר',
     'version_desc': '',
     'version_type': '0',
     'hospital_type': '2',
     'active': True,
     'measure_names': [],
     'measure': [],
     'measures': [{'_id': {'$oid': '5c0d3fd6326f422ea4939bfe'}, 'measure_name': 'מדד חדש'}]

     }
# print(is_valid_code('123.23.765'))

#print(is_valid_number(234))
print(is_valid_update_version(d))