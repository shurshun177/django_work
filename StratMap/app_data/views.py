from . models import Version, Measure, DecryptionTables
from django.http import HttpResponse, JsonResponse
from . database import DataBase
from .odm import MongoDBManager
import bson
import json
from bson import ObjectId
from bson.json_util import dumps

db = DataBase()
db.connect()


def del_vers(request, vers_id):
    if request.method == 'PUT':
        k = 'Version_del property was updated, arg is {}'.format(vers_id)
        return HttpResponse(k)


def del_measure(request, measure_id):
    if request.method == 'PUT':
        k = 'Measure_del property was updated, arg is {}'.format(measure_id)
        return HttpResponse(k)


def index(request):
    query = db.get_all('app_data_version')
    items = None
    if query.count()>0:
        items = dumps({'items':query})
    result = json.loads(items) if items else {'items':[]}
    return JsonResponse(result)

def index_0(request):
    if request.method == 'GET':
        id = request.body
        return HttpResponse(id)
    else:
        return HttpResponse('Request method must be GET')


def versions(request):
    if request.method == 'GET':
        query = db.find("app_data_version")
        items = None
        if query.count() > 0:
            items = dumps({'items': query})
        result = json.loads(items) if items else {'items': []}
        return JsonResponse(result)
    elif request.method == 'POST':
        return HttpResponse('Create Version POST request')


def get_version(request, vers_id):
    if request.method == 'GET':
        mycol = DataBase("app_data_version")
        query = mycol.get_all(
            '_id',
            'version_desc',
            'measure_id',
            'cancel',
            'version_type',
            'cancel_date',
            'cancel_user',
            'change_date',
            'change_user',
            'create_user',
            id=int(vers_id)
        )
        vers_dict = [dict(i) for i in query]
        if vers_dict:
            return JsonResponse(vers_dict, safe=False)
        else:
            return HttpResponse(status=404, content='No such version')


def measures(request):
    if request.method == 'GET':
        query = db.find("app_data_measure")
        items = None
        if query.count() > 0:
            items = dumps({'items': query})
        result = json.loads(items) if items else {'items': []}
        return JsonResponse(result)
    elif request.method == 'POST':
        return HttpResponse('Create Measure POST request')


def get_measure(request):
    if request.method == 'GET':
        _id = request.body.decode().split('=')[-1]
        if not db.is_valid_id(_id):
            return HttpResponse(status=400, content='Invalid id')
        query = db.get_by_id("app_data_measure", _id)
        items = None
        if query.count() > 0:
            items = dumps({'items': query})
        else:
            return HttpResponse(status=404, content='No such measure')
        result = json.loads(items) if items else {'items': []}
        return JsonResponse(result)


def update_measure(request):
    if request.method == 'PUT':
        return HttpResponse('Update Measure PUT request')


def update_version(request):
    if request.method == 'PUT':
        return HttpResponse('Update Version PUT request')




