import json

import requests
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.

from railwayadmin.settings import MIDDLEWARE_URL, API_HEADERS
from station.forms import CreateStationForm
from utils.helpers import check_session, get_headers


@check_session()
def index(request):
    return render(request, 'station/index.html', {})


@check_session()
def create(request):
    header = get_headers(request)
    if request.method == 'POST':
        station_id = request.POST['identifier']
        form = CreateStationForm(request.POST)
        if form.is_valid():
            if station_id:
                requests.post(MIDDLEWARE_URL + "/station/edit", data=json.dumps(form.as_dict(True)),
                              headers=header)
            else:
                requests.post(MIDDLEWARE_URL + "/station/create", data=json.dumps(form.as_dict()), headers=header)
            return HttpResponseRedirect('/station')
    else:
        # station_id = request.GET['id']
        # if station_id:
        #     form = CreateStationForm(request.GET)
        # else:
        form = CreateStationForm()

    station_id = request.GET.get('id')
    if station_id:
        station = requests.post(MIDDLEWARE_URL + "/station/get/" + station_id, headers=header)
        form = CreateStationForm(json.loads(station.content.decode()))
    return render(request, 'station/create.html', {'form': form})


@check_session()
def view(request):
    station_id = request.GET.get('id')
    header = get_headers(request)
    station_data = requests.post(MIDDLEWARE_URL + "/station/get/" + station_id, headers=header)
    return render(request, 'station/view.html', {'stationData': json.loads(station_data.content.decode())})


@check_session()
def table_list(request):
    data = {
        "filters": json.loads(request.body)
    }
    header = get_headers(request)
    dataTableRow = requests.post(MIDDLEWARE_URL + "/station/admin/list1", data=json.dumps(data), headers=header)
    return JsonResponse(json.loads(dataTableRow.content.decode()))


@check_session()
def activate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if data['id']:
            header = get_headers(request)
            r_data = requests.post(MIDDLEWARE_URL + "/station/activate", data=json.dumps(data), headers=header)
            if r_data.status_code == 200:
                return HttpResponse()
            else:

                return HttpResponse(status=r_data.status_code)
        else:
            return HttpResponse(status=404)

# def search(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode())
#         if data['id']:
#             data = dict()
#             data["foo"] = "bar"
#             header = API_HEADERS
#             data = requests.post(MIDDLEWARE_URL + "/station/admin/list1", data=json.dumps(data), headers=header)
#             return JsonResponse(data)
