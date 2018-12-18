from datetime import datetime as d
def is_valid_code(measure_code):
    t = '0123456789.'
    test_func = map(lambda x: x in t, measure_code)
    c = False not in test_func
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
        'digit_num',
        'separate_thousands',
        'active'
    )
    for i in fields:
        if not data[i]:
            return False
    return True


def is_valid_version(data):
    fields = (
        'version_number',
        'version_name',
        'version_type',
        'hospital_type',
        'active',
        # additional field measure
    )
    for i in fields:
        if not data[i]:
            return False
    return True


d = {'version_number': '1002',
     'version_name': '',
     'version_desc': '',
     'version_type': 'gfd',
     'hospital_type': '1',
     'active': True,
     'business_topic': ''
     }
print(is_valid_version(d))


#print(is_valid_number(234))