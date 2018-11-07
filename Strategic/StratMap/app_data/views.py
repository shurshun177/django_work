#from django.shortcuts import render
from . models import Version, Measure, DecryptionTables
from django.http import HttpResponse, Http404



def index(request):

    r = DecryptionTables.objects.all()[1].values_list[1]
    r_ver = DecryptionTables.objects.all()[2].values_list[1]['type']
    l = len(DecryptionTables.objects.all()[2].values_list)
    a = [DecryptionTables.objects.all()[2].values_list[i]['type'] for i in range(l)]
    return HttpResponse('It works {}'.format(a))

def get_versions(request):
    q = Version.objects.all()
    return HttpResponse('Now you have versions: {}'.format(q))


def get_version(request):
    pass


def get_measures(request):
    q = Measure.objects.all()
    return HttpResponse('Now you have measures: {}'.format(q))


def get_measure(request):
    pass


def create_version(request):
    pass


def cerate_measure(request):
    pass


def update_version(request):
    pass


def update_measure(request):
    pass
