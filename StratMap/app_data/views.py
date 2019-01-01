from django.http import HttpResponse, JsonResponse
from . database import DataBase
import datetime
import json
from bson.json_util import dumps, loads
from django.views.decorators.http import require_http_methods, require_GET
from . valid import is_valid_code, is_valid_version, is_valid_update_version,\
    is_valid_measure, is_valid_update_measure
from bson.objectid import _ord
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
            return HttpResponse(status=404, content='No such version')
    except:
        return HttpResponse(status=422, content='Invalid id')
    return HttpResponse(query)


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
            return HttpResponse(status=404, content='No such measure')
    except:
        return HttpResponse(status=422, content='Invalid id')
    return HttpResponse(query)


def index(request):
    query = db.get_all('app_data_version')
    items = None
    if query.count()>0:
        items = dumps({'items':query})
    result = json.loads(items) if items else {'items':[]}
    return JsonResponse(result)


@require_http_methods(['GET', 'POST'])
def index_0(request):
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
            return HttpResponse(status=422, content='Mandatory fields are empty')
        try:
            number = int(data['version_number'])
        except ValueError:
            return HttpResponse(status=400, content='Number must be integer')
        current_date = datetime.datetime.utcnow()
        data['version_number'] = number
        data['cancel'] = False
        data['create_date'] = current_date
        data['create_user'] = 'Shnur'
        try:
            query = db.post('app_data_version', data)
        except:
            return HttpResponse(status=422, content='Database exeption')
        return HttpResponse(query)


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
        measures = [{'id': i['_id']['$oid'], 'measure_name': i['measure_name']} for i in data['measures']]
        print(data)
        if not is_valid_version(data):

            return HttpResponse(status=422, content='Mandatory fields are empty')
        try:
            number = int(data['version_number'])
        except ValueError:

            return HttpResponse(status=400, content='Number must be integer')
        current_date = datetime.datetime.utcnow()
        data['version_number'] = number
        data['cancel'] = False
        data['create_date'] = current_date
        data['create_user'] = 'Shnur'
        data['measure'] = measures
        print(data)
        try:
            query = db.post('app_data_version', data)
        except:
            print('Noviy povorot')
            return HttpResponse(status=422, content='Database exeption')
        return HttpResponse(query)


@require_GET
def get_version(request, vers_id):
    try:
        query = db.get_by_id('app_data_version', vers_id)
    except:
        return HttpResponse(status=422, content='Invalid id')
    items = None
    if query.count() > 0:
        items = dumps({'items': query})
    else:
        return HttpResponse(status=404, content='No such version')
    result = json.loads(items) if items else {'items': []}
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
            return HttpResponse(status=422, content='Empty mandatory fields')
        if not is_valid_code(data['measure_code']):
            return HttpResponse(status=400)
        current_date = datetime.datetime.utcnow()
        data['cancel'] = False
        data['create_date'] = current_date
        data['create_user'] = 'Sheldon'
        try:
            query = db.post('app_data_measure', data)
        except:
            return HttpResponse(status=422, content='Unique fields exist')
        return HttpResponse(query)


@require_GET
def get_measure(request, id):
    try:
        query = db.get_by_id('app_data_measure', id)
    except:
        return HttpResponse(status=422, content='Invalid id')
    items = None
    if query.count() > 0:
        items = dumps({'items': query})
    else:
        return HttpResponse(status=404, content='No such measure')
    result = json.loads(items) if items else {'items': []}
    return JsonResponse(result)


@require_http_methods(['PUT'])
def update_measure(request, measure_id):

    body = request.body
    data = json.loads(body)
    if not is_valid_update_measure(data):
        return HttpResponse(status=422, content='Mandatory fields are empty')
    current_date = datetime.datetime.utcnow()
    data['change_date'] = current_date
    data['change_user'] = 'Terminator'
    try:
        query = db.update('app_data_measure', data, measure_id)
        if query is None:
            return HttpResponse(status=404, content='No such measure')
    except:
        return HttpResponse(status=422, content='Invalid id')
    return HttpResponse(query)


@require_http_methods(['PUT'])
def update_version(request, vers_id):
    body = request.body
    data = json.loads(body)
    if not is_valid_update_version(data):
        return HttpResponse(status=422, content='Mandatory fields are empty')
    current_date = datetime.datetime.utcnow()
    data['change_date'] = current_date
    data['change_user'] = 'Tarsan'
    try:
        query = db.update('app_data_version', data, vers_id)
        if query is None:
            return HttpResponse(status=404, content='No such version')
    except:
        return HttpResponse(status=422, content='Invalid id')
    return HttpResponse(query)


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
        return HttpResponse(status=422)
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
        return HttpResponse(status=422)
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
        return HttpResponse(status=422)
    val = [i.get('version_number') for i in query][0]
    res = {'vers_number': val + 1}
    return JsonResponse(res)




