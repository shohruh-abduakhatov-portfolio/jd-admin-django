import json

import requests
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from language.forms import CreateLanguageForm
from railwayadmin.settings import MIDDLEWARE_URL, API_HEADERS
from utils.helpers import check_session, get_headers


@check_session()
def index(request):
    return render(request, 'language/index.html', {})


@check_session()
def create(request):
    header = get_headers(request)
    if request.method == 'POST':
        language_id = request.POST['identifier']
        form = CreateLanguageForm(request.POST)
        if form.is_valid():
            if language_id:
                requests.post(MIDDLEWARE_URL + "/language/edit", data=json.dumps(form.as_dict(True)), headers=header)
            else:
                requests.post(MIDDLEWARE_URL + "/language/create", data=json.dumps(form.as_dict()), headers=header)
            return HttpResponseRedirect('/language')
    else:
        form = CreateLanguageForm()

    language_id = request.GET.get('id')
    if language_id:
        language = requests.post(MIDDLEWARE_URL + "/language/get/"+language_id, headers=header)
        form = CreateLanguageForm(json.loads(language.content.decode()))
    return render(request, 'language/create.html', {'form': form})


@check_session()
def view(request):
    language_id = request.GET.get('id')
    header = get_headers(request)
    language_data = requests.post(MIDDLEWARE_URL + "/language/get/"+language_id, headers=header)
    return render(request, 'language/view.html', {'languageData': json.loads(language_data.content.decode())})


@check_session()
def table_list(request):
    data = {
        "filters": json.loads(request.body)
    }
    header = get_headers(request)
    dataTableRow = requests.post(MIDDLEWARE_URL + "/language/list", data=json.dumps(data), headers=header)
    return JsonResponse(json.loads(dataTableRow.content.decode()))


@check_session()
def activate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if data['id']:
            header = get_headers(request)
            r_data = requests.post(MIDDLEWARE_URL + "/language/activate", data=json.dumps(data), headers=header)
            if r_data.status_code == 200:
                return HttpResponse()
            else:

                return HttpResponse(status=r_data.status_code)
        else:
            return HttpResponse(status=404)
