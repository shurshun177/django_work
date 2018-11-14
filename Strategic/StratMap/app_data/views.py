from . models import Version, Measure, DecryptionTables
from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from . database import DataBase


def index(request):
    mycol = DataBase("app_data_version")
    query = mycol.get_all('_id', 'cancel', active=True, version_number=1000)
    dict_1 = [dict(i) for i in query]
    return HttpResponse(HttpRequest.scheme)


def get_versions(request):
    mycol = DataBase("app_data_version")
    query = mycol.get_all('_id') #'_id' must be equal to 0 always
    vers_dict = [dict(i) for i in query] #it isn`t json serializable
    return JsonResponse(vers_dict, safe=False)


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
    return JsonResponse(vers_dict, safe=False)


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
