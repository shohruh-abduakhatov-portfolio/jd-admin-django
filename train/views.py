import json

import requests
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.

from railwayadmin.settings import MIDDLEWARE_URL, API_HEADERS
from train.forms import CreateTrainForm
from utils.helpers import check_session, get_headers


@check_session()
def index(request):
    return render(request, 'train/index.html', {})


@check_session()
def create(request):
    header = get_headers(request)
    if request.method == 'POST':
        train_id = request.POST['identifier']
        form = CreateTrainForm(request.POST)
        if form.is_valid():
            if train_id:
                requests.post(MIDDLEWARE_URL + "/train/update", data=json.dumps(form.as_dict(True)), headers=header)
            else:
                requests.post(MIDDLEWARE_URL + "/train/create", data=json.dumps(form.as_dict()), headers=header)
            return HttpResponseRedirect('/train')
    else:
        # train_id = request.GET['id']
        # if train_id:
        #     form = CreateTrainForm(request.GET)
        # else:
        form = CreateTrainForm()

    train_id = request.GET.get('id')
    if train_id:
        train = requests.post(MIDDLEWARE_URL + "/train/get/"+train_id, headers={'Accept': 'application/json'})
        form = CreateTrainForm(json.loads(train.content.decode()))
    return render(request, 'train/create.html', {'form': form})


@check_session()
def view(request):
    header = get_headers(request)
    train_id = request.GET.get('id')
    train_data = requests.post(MIDDLEWARE_URL + "/train/get/"+train_id, headers=header)
    return render(request, 'train/view.html', {'trainData': json.loads(train_data.content.decode())})


@check_session()
def table_list(request):
    data = {
        "filters": json.loads(request.body)
    }
    header = get_headers(request)
    dataTableRow = requests.post(MIDDLEWARE_URL + "/train/list", data=json.dumps(data), headers=header)
    return JsonResponse(json.loads(dataTableRow.content.decode()))


@check_session()
def activate(request):
    header = get_headers(request)
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if data['id']:
            r_data = requests.post(MIDDLEWARE_URL + "/train/activate", data=json.dumps(data), headers=header)
            if r_data.status_code == 200:
                return HttpResponse()
            else:

                return HttpResponse(status=r_data.status_code)
        else:
            return HttpResponse(status=404)

