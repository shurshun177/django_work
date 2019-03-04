from django.http import HttpResponse, JsonResponse
from . database import DataBase
import datetime
import json
from bson.json_util import dumps, loads
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from . valid import is_valid_code, is_valid_version, is_valid_update_version,\
    is_valid_measure, is_valid_update_measure
import os


db = DataBase()
db.connect()


@require_http_methods(['PUT'])
def del_vers(request, vers_id):

    current_date = datetime.datetime.utcnow()
    data = dict()
    data['cancel'] = True
    data['cancel_date'] = current_date
    data['cancel_user'] = 'Rasgildyai'
    try:
        query = db.update('app_data_version', data, vers_id)
        if query is None:
            response = {'status': 'failed', 'reason': 'No such version'}
            return JsonResponse(status=404, data=response)
    except:
        response = {'status': 'failed', 'reason': 'Invalid id'}
        return JsonResponse(status=422, data=response)
    response = {'status': 'success', 'message': 'Cancel field was updated'}
    return JsonResponse(response)


@require_http_methods(['PUT'])
def del_measure(request, measure_id):
    current_date = datetime.datetime.utcnow()
    data = dict()
    data['cancel'] = True
    data['cancel_date'] = current_date
    data['cancel_user'] = 'Rasgildyai'
    try:
        query = db.update('app_data_measure', data, measure_id)
        if query is None:
            response = {'status': 'failed', 'reason': 'No such measure'}
            return JsonResponse(status=404, data=response)
    except:
        response = {'status': 'failed', 'reason': 'Invalid id'}
        return JsonResponse(status=422, data=response)
    response = {'status': 'success', 'message': 'Cancel field was updated'}
    return JsonResponse(response)

@require_POST
def entry(request):
    body = request.body
    data = json.loads(body)
    cwd = os.getcwd()
    name = data['name']['name']
    password = data['name']['password']
    with open(os.path.join(cwd, r'users.json'), 'r') as f:
        d = f.read()
    j = json.loads(d)
    list_users = j.get('users')
    l = [i.get('type') for i in list_users if i.get('user') == name and i.get('password') == password]
    if l:
        user_type = l[0]
        return JsonResponse({'status': 'accepted', 'user': name, 'user_type': user_type}, status=200)
    else:
        return JsonResponse({'status': 'denied'}, status=400)

@require_POST
def index_0(request):
    body = request.body
    data = json.loads(body)
    current_date = datetime.datetime.utcnow()
    krit = {
        'measure_code': data.get('measure_code'),
        'hospital_type': data.get('hospital_type'),
        'year': data.get('year')
    }
    l = db.exists('app_data_nationalaverage', krit)

    if l == 0:
        query = {'measure_code': data.get('measure_code'),
                'year': data.get('year'),
                'hospital_type': data.get('hospital_type'),
                'actual_value': [
                    {
                        'national_measure': data.get('national_measure'),
                        'create_data': current_date,
                        'create_user': '',
                        'change_date': '',
                        'change_user': ''
                    },
                    {
                        'average_measure': data.get('average_measure'),
                        'create_data': current_date,
                        'create_user': '',
                        'change_date': '',
                        'change_user': ''
                    },
                ]}
        try:
            db.post('app_data_nationalaverage', data=query)
        except:
            resp = {'status': 'failed'}
            return JsonResponse(resp, status=400)
        return JsonResponse({'status': 'created'})
    else:
        if data.get('national_measure') and data.get('average_measure'):
            query = {'actual_value.0.national_measure': data.get('national_measure'),
                    'actual_value.0.change_date': current_date,
                    'actual_value.1.average_measure': data.get('average_measure'),
                    'actual_value.1.change_date': current_date,
                    }
            try:
                db.update('app_data_nationalaverage', data=query, req=krit)
            except:
                resp = {'status': 'failed'}
                return JsonResponse(resp, status=400)
            return JsonResponse({'status': 'updated'})
        elif data.get('national_measure'):
            query = {'actual_value.0.national_measure': data.get('national_measure'),
                    'actual_value.0.change_date': current_date
                    }
            try:
                db.update('app_data_nationalaverage', data=query, req=krit)
            except:
                resp = {'status': 'failed'}
                return JsonResponse(resp, status=400)
            return JsonResponse({'status': 'updated'})
        elif data.get('average_measure'):
            query = {'actual_value.1.average_measure': data.get('average_measure'),
                    'actual_value.1.change_date': current_date,
                    }
            try:
                db.update('app_data_nationalaverage', data=query, req=krit)
            except:
                resp = {'status': 'failed'}
                return JsonResponse(resp, status=400)
            return JsonResponse({'status': 'updated'})


@require_http_methods(['GET', 'POST'])
def versions(request):
    if request.method == 'GET':
        query = db.find("app_data_version", {'cancel': False})
        items = None
        if query.count() > 0:
            items = dumps({'items': query})
        result = json.loads(items) if items else {'items': []}
        return JsonResponse(result)
    elif request.method == 'POST':
        body = request.body
        data = json.loads(body)
        if not is_valid_version(data):

            response = {'status': 'failed', 'reason': 'Mandatory fields are empty'}
            return JsonResponse(status=422, data=response)

        current_date = datetime.datetime.utcnow()

        data['cancel'] = False
        data['create_date'] = current_date
        data['create_user'] = 'Shnur'
        try:
            db.post('app_data_version', data)
        except:

            response = {'status': 'failed', 'reason': 'Database exeption'}
            return JsonResponse(status=422, data=response)
        response = {'status': 'success', 'message': 'Version was saved successfully'}
        return JsonResponse(response)


@require_GET
def get_version(request, vers_id):
    try:
        query = db.get_by_id('app_data_version', vers_id)
    except:
        response = {'status': 'failed', 'reason': 'Invalid id'}
        return JsonResponse(status=422, data=response)
    items = None
    if query.count() > 0:
        items = dumps({'items': query})
    else:
        response = {'status': 'failed', 'reason': 'No such version'}
        return JsonResponse(status=404, data=response)
    result = json.loads(items) if items else {'items': []}
    # print(result)
    return JsonResponse(result)


@require_http_methods(['GET', 'POST'])
def measures(request):
    if request.method == 'GET':
        query = db.find("app_data_measure", {'cancel': False})
        items = None
        if query.count() > 0:
            items = dumps({'items': query})
        result = json.loads(items) if items else {'items': []}
        return JsonResponse(result)
    elif request.method == 'POST':
        body = request.body
        data = json.loads(body)
        if not is_valid_measure(data):
            response = {'status': 'failed', 'reason': 'Empty mandatory fields'}

            return JsonResponse(status=422, data=response)
        if not is_valid_code(data['measure_code']):
            response = {'status': 'failed', 'reason': 'Invalid measure code'}
            return JsonResponse(status=400, data=response)
        current_date = datetime.datetime.utcnow()
        data['cancel'] = False
        data['create_date'] = current_date
        data['create_user'] = 'Sheldon'
        try:
            db.post('app_data_measure', data)
        except:
            response = {'status': 'failed', 'reason': 'Unique fields already exist'}

            return JsonResponse(status=422, data=response)
        response = {'status': 'success', 'message': 'Measure was saved successfully'}
        return JsonResponse(response)


@require_GET
def get_measure(request, id):
    try:
        query = db.get_by_id('app_data_measure', id)
    except:
        response = {'status': 'failed', 'reason': 'Invalid id'}
        return JsonResponse(status=422, data=response)
    items = None
    if query.count() > 0:
        items = dumps({'items': query})
    else:
        response = {'status': 'failed', 'reason': 'No such measure'}
        return JsonResponse(status=404, data=response)
    result = json.loads(items) if items else {'items': []}
    return JsonResponse(result)


@require_http_methods(['PUT'])
def update_measure(request, measure_id):

    body = request.body
    data = json.loads(body)
    if not is_valid_update_measure(data):
        response = {'status': 'failed', 'reason': 'Mandatory fields are empty'}
        return JsonResponse(status=422, data=response)
    current_date = datetime.datetime.utcnow()
    data['change_date'] = current_date
    data['change_user'] = 'Terminator'
    try:
        query = db.update('app_data_measure', data, measure_id)
        if query is None:
            response = {'status': 'failed', 'reason': 'No such measure'}
            return JsonResponse(status=404, data=response)
    except:
        response = {'status': 'failed', 'reason': 'Invalid id'}
        return JsonResponse(status=422, data=response)
    response = {'status': 'success', 'message': 'Measure was updated successfully'}
    return JsonResponse(response)


@require_http_methods(['PUT'])
def update_version(request, vers_id):
    body = request.body
    data = json.loads(body)

    if not is_valid_update_version(data):

        response = {'status': 'failed', 'reason': 'Mandatory fields are empty'}
        return JsonResponse(status=422, data=response)
    current_date = datetime.datetime.utcnow()
    data['change_date'] = current_date
    data['change_user'] = 'Tarsan'
    try:
        query = db.update('app_data_version', data, vers_id)
        if query is None:
            response = {'status': 'failed', 'reason': 'No such version'}
            return JsonResponse(status=404, data=response)
    except:

        response = {'status': 'failed', 'reason': 'Invalid id'}
        return JsonResponse(status=422, data=response)
    response = {'status': 'success', 'message': 'Version was updated successfully'}
    return JsonResponse(response)


@require_GET
def available_measures(request, topic, code):

    try:
        query = db.find(
            "app_data_measure",
            {
                'active': True, 'cancel': False,
                'hospital_type': code,
                'business_topic': topic
            },
            fields={'measure_name'})
    except:
        response = {'status': 'failed', 'reason': 'No available measures'}
        return JsonResponse(status=422, data=response)
    items = None
    if query.count() > 0:
        k = dumps(query)
        measures = [{'id': i['_id']['$oid'], 'measure_name': i['measure_name']} for i in json.loads(k)]
        items = {'items': measures}
    result = items if items else {'items': []}
    return JsonResponse(result)


@require_GET
def get_dec(request):

    try:
        query = db.find('app_data_decryptiontables')
    except:
        response = {'status': 'failed', 'reason': 'Database exception'}
        return JsonResponse(status=422, data=response)
    items = None
    if query.count() > 0:
        items = dumps({'items': query})
    result = json.loads(items) if items else {'items': []}
    return JsonResponse(result, safe=False)


@require_GET
def last_version(request):
    col = 'app_data_version'
    key = 'create_date'

    try:
        query = db.get(col, sorted_by=key, ascending=False, limit=1)
    except:
        response = {'status': 'failed', 'reason': 'Database exception'}
        return JsonResponse(status=422, data=response)
    if query.count() > 0:
        val = [i.get('version_number') for i in query][0]

        val = int(val) + 1
        res = {'vers_number': str(val)}
    else:
        res = {'vers_number': '1000'}
    return JsonResponse(res)


@require_GET
def versionSearch(request, text):
    col = 'app_data_version'
    search_field = 'version_name'
    text_str = '.*{}.*'.format(text)
    query = {'cancel': False, search_field: {'$regex': text_str}}
    res = db.find(col, query)

    if res.count() == 0:
        search_field_1 = 'version_number'
        text_1 = '.*{}.*'.format(text)
        query_1 = {'cancel': False, search_field_1: {'$regex': text_1}}
        res = db.find(col, query_1)
    items = None
    if res.count() > 0:
        items = dumps({'items': res})
    result = json.loads(items) if items else {'items': []}
    return JsonResponse(result)


@require_GET
def measureSearch(request, text):

    col = 'app_data_measure'
    search_field = 'measure_code'
    text = '.*{}.*'.format(text)
    query = {'cancel': False, search_field: {'$regex': text}}
    res = db.find(col, query)
    if res.count() == 0:
        search_field_1 = 'measure_name'
        text_1 = '.*{}.*'.format(text)
        query_1 = {'cancel': False, search_field_1: {'$regex': text_1}}
        res = db.find(col, query_1)
    items = None
    if res.count() > 0:
        items = dumps({'items': res})
    result = json.loads(items) if items else {'items': []}
    return JsonResponse(result)


@require_GET
def national_average(request, type, year):
    last_year = str(int(year) - 1)
    data = {'type': type, 'last_year': last_year, 'year': year}
    filt = {
        'year': {'$in': [
            last_year, year
        ]
        },
        'hospital_type': type
    }
    measure_filter = {'cancel': False}
    measure_fields = {'measure_code': 1, 'measure_name': 1}
    actual_values = [i for i in db.find('app_data_nationalaverage', filt)]
    measure_codes = [i for i in db.find('app_data_measure', measure_filter, measure_fields)]
    for j in actual_values:
        for i in measure_codes:
            if i.get('measure_code') == j.get('measure_code'):
                i[j.get('year')] = j.setdefault('actual_value')
    items = None
    if len(measure_codes) > 0:
        items = dumps({'items': measure_codes})
    result = json.loads(items) if items else {'items': []}
    return JsonResponse(result)


@require_GET
def getHosp(request, hosp_type):

    if hosp_type == '1':
        f = 'type_1'
    elif hosp_type == '2':
        f = 'type_2'
    elif hosp_type == '3':
        f = 'type_3'
    else:
        return JsonResponse({'status': 'failed', 'reason': 'wrong number'}, status=400)
    col = 'app_data_decryptiontables'
    data = {
        'name': 'hospital_codes'
    }
    fields = {f: 1}
    res = db.find(col, filter=data, fields={f:1})
    items = dumps({'items': res})
    result = json.loads(items) if items else {'items': []}
    return JsonResponse(result)


@require_GET
def division(request, hosp, topic):
    col = 'app_data_measure'
    print(hosp, topic)
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

    }
    # measures = [i for i in db.find(col, filter, fields)]
    query = db.find(col=col, filter=filter, fields=fields)
    items = None
    if query.count() > 0:
        items = dumps({'items': query})
    result = json.loads(items) if items else {'items': []}
    return JsonResponse(result)


@require_GET
def hospReport(request, hosp, topic):
    filter = {

        'business_topic': topic,

        'is_division': False,
        'cancel': False
    }
    fields = {
        'measure_name': 1,
        'measure_code': 1,

    }
    # measures = [i for i in db.find(col, filter, fields)]
    query = db.find(col='app_data_measure', filter=filter, fields=fields)
    items = None
    if query.count() > 0:
        items = dumps({'items': query})
    result = json.loads(items) if items else {'items': []}
    return JsonResponse(result)