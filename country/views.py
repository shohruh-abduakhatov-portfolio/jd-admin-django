import json

import requests
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from country.forms import CreateCountryForm
from railwayadmin.settings import MIDDLEWARE_URL, API_HEADERS
from utils.helpers import check_session, get_headers


@check_session()
def index(request):
    return render(request, 'country/index.html', {})


@check_session()
def create(request):
    header = get_headers(request)
    if request.method == 'POST':
        country_id = request.POST['identifier']
        form = CreateCountryForm(request.POST)
        if form.is_valid():
            if country_id:
                requests.post(MIDDLEWARE_URL + "/country/edit", data=json.dumps(form.as_dict(True)),
                              headers=header)
            else:
                requests.post(MIDDLEWARE_URL + "/country/create", data=json.dumps(form.as_dict()), headers=header)
            return HttpResponseRedirect('/country')
    else:
        form = CreateCountryForm()

    country_id = request.GET.get('id')
    if country_id:
        country = requests.post(MIDDLEWARE_URL + "/country/get/"+country_id, headers=header)
        form = CreateCountryForm(json.loads(country.content.decode()))
    return render(request, 'country/create.html', {'form': form})


@check_session()
def view(request):
    country_id = request.GET.get('id')
    header = get_headers(request)
    country_data = requests.post(MIDDLEWARE_URL + "/country/get/"+country_id, headers=header)
    return render(request, 'country/view.html', {'countryData': json.loads(country_data.content.decode())})


@check_session()
def table_list(request):
    data = {
        "filters": json.loads(request.body)
    }
    header = get_headers(request)
    dataTableRow = requests.post(MIDDLEWARE_URL + "/country/list", data=json.dumps(data), headers=header)
    return JsonResponse(json.loads(dataTableRow.content.decode()))


@check_session()
def activate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if data['countryId']:
            header = get_headers(request)
            r_data = requests.post(MIDDLEWARE_URL + "/country/activate", data=json.dumps(data), headers=header)
            if r_data.status_code == 200:
                return HttpResponse()
            else:

                return HttpResponse(status=r_data.status_code)
        else:
            return HttpResponse(status=404)
