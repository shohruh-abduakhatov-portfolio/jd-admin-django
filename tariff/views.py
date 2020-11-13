import json

import requests
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from tariff.forms import CreateTariffForm
from railwayadmin.settings import MIDDLEWARE_URL, API_HEADERS
from utils.helpers import check_session, get_headers


@check_session()
def index(request):
    return render(request, 'tariff/index.html', {})


@check_session()
def create(request):
    header = get_headers(request)
    if request.method == 'POST':
        tariff_id = request.POST['identifier']
        form = CreateTariffForm(request.POST)
        if form.is_valid():
            if tariff_id:
                requests.post(MIDDLEWARE_URL + "/tariff/edit", data=json.dumps(form.as_dict(True)), headers=header)
            else:
                requests.post(MIDDLEWARE_URL + "/tariff/create", data=json.dumps(form.as_dict()), headers=header)
            return HttpResponseRedirect('/tariff')
    else:
        form = CreateTariffForm()

    tariff_id = request.GET.get('id')
    if tariff_id:
        tariff = requests.post(MIDDLEWARE_URL + "/tariff/get/"+tariff_id, headers=header)
        form = CreateTariffForm(json.loads(tariff.content.decode()))
    return render(request, 'tariff/create.html', {'form': form})


@check_session()
def view(request):
    tariff_id = request.GET.get('id')
    header = get_headers(request)
    tariff_data = requests.post(MIDDLEWARE_URL + "/tariff/get/"+tariff_id, headers=header)
    return render(request, 'tariff/view.html', {'tariffData': json.loads(tariff_data.content.decode())})


@check_session()
def table_list(request):
    data = {
        "filters": json.loads(request.body)
    }
    header = get_headers(request)
    dataTableRow = requests.post(MIDDLEWARE_URL + "/tariff/list", data=json.dumps(data), headers=header)
    return JsonResponse(json.loads(dataTableRow.content.decode()))


@check_session()
def activate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if data['tariffId']:
            header = get_headers(request)
            r_data = requests.post(MIDDLEWARE_URL + "/tariff/activate", data=json.dumps(data), headers=header)
            if r_data.status_code == 200:
                return HttpResponse()
            else:

                return HttpResponse(status=r_data.status_code)
        else:
            return HttpResponse(status=404)
