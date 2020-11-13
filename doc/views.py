import json

import requests
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from doc.forms import CreateDocForm
from railwayadmin.settings import MIDDLEWARE_URL, API_HEADERS
from utils.helpers import check_session, get_headers


@check_session()
def index(request):
    return render(request, 'doc/index.html', {})


@check_session()
def create(request):
    header = get_headers(request)
    if request.method == 'POST':
        doc_id = request.POST['identifier']
        form = CreateDocForm(request.POST)
        if form.is_valid():
            if doc_id:
                requests.post(MIDDLEWARE_URL + "/doc/edit", data=json.dumps(form.as_dict(True)), headers=header)
            else:
                requests.post(MIDDLEWARE_URL + "/doc/create", data=json.dumps(form.as_dict()), headers=header)
            return HttpResponseRedirect('/doc')
    else:
        form = CreateDocForm()

    doc_id = request.GET.get('id')
    if doc_id:
        doc = requests.post(MIDDLEWARE_URL + "/doc/get/"+doc_id, headers=header)
        form = CreateDocForm(json.loads(doc.content.decode()))
    return render(request, 'doc/create.html', {'form': form})


@check_session()
def view(request):
    doc_id = request.GET.get('id')
    header = get_headers(request)
    doc_data = requests.post(MIDDLEWARE_URL + "/doc/get/"+doc_id, headers=header)
    return render(request, 'doc/view.html', {'docData': json.loads(doc_data.content.decode())})


@check_session()
def table_list(request):
    data = {
        "filters": json.loads(request.body)
    }
    header = get_headers(request)
    dataTableRow = requests.post(MIDDLEWARE_URL + "/doc/list", data=json.dumps(data), headers=header)
    return JsonResponse(json.loads(dataTableRow.content.decode()))


@check_session()
def activate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if data['docId']:
            header = get_headers(request)
            r_data = requests.post(MIDDLEWARE_URL + "/doc/activate", data=json.dumps(data), headers=header)
            if r_data.status_code == 200:
                return HttpResponse()
            else:

                return HttpResponse(status=r_data.status_code)
        else:
            return HttpResponse(status=404)
