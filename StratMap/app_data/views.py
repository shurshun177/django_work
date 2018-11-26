from . models import Version, Measure, DecryptionTables
from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from . database import DataBase
import json

def post_test(request):

    #a = json.loads(request.body)
    t = Version.objects.all()
    return HttpResponse(t)

def index(request):
    k = request.user
    #return JsonResponse(k, safe=False)
    return HttpResponse(str(k))


def versions(request):
    if request.method == 'GET':
        mycol = DataBase("app_data_version")
        if
        query = mycol.get_all() #'_id' must be equal to 0 always
        vers_dict = [dict(i) for i in query]  # it isn`t json serializable
        return JsonResponse(vers_dict, safe=False)
    elif request.method == 'PUT':
        return HttpResponse('hgfgfdd')


def get_version(request, vers_id):
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
        return HttpResponse(status=404, content='No such id')


def get_measures(request):
    mycol = DataBase("app_data_measure")
    query = mycol.get_all('_id')  # '_id' must be equal to 0 always
    vers_dict = [dict(i) for i in query]  # it isn`t json serializable
    return JsonResponse(vers_dict, safe=False)


def get_measure(request, measure_id):
    mycol = DataBase("app_data_measure")
    query = mycol.get_all('_id', id=int(measure_id))
    vers_dict = [dict(i) for i in query]
    return JsonResponse(vers_dict, safe=False)


def create_version(request):
    pass


def cerate_measure(request):
    pass


def update_version(request):
    pass


def update_measure(request):
    pass
