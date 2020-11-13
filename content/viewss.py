import json

import requests
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.shortcuts import render

# Create your views here.
from label.forms import CreateLabelForm
from railwayadmin.settings import MIDDLEWARE_URL, API_HEADERS
from utils.helpers import check_session, get_headers


@check_session()
def index(request):
    return render(request, 'label/index.html', {})


@check_session()
def create(request):
    header = get_headers(request)
    if request.method == 'POST':
        label_id = request.POST['identifier']
        form = CreateLabelForm(request.POST)
        if form.is_valid():
            if label_id:
                data = form.as_dict(True)
                data['contentId'] = request.GET['content_id']
                response = requests.post(MIDDLEWARE_URL + "/content/label/edit", data=json.dumps(data), headers=header)
            else:
                data = form.as_dict()
                data['contentId'] = request.GET['content_id']
                response = requests.post(MIDDLEWARE_URL + "/content/label/create", data=json.dumps(data), headers=header)
            if response.status_code == 500:
                return HttpResponseServerError()
            return HttpResponseRedirect('/content')
    else:
        form = CreateLabelForm()
        # form.fields['content_identifier'].empty_value = request.GET['id']

    label_id = request.GET.get('id')
    if label_id:
        label = requests.post(MIDDLEWARE_URL + "/content/label/get/"+label_id, headers=header)
        form = CreateLabelForm(json.loads(label.content.decode()))
    return render(request, 'label/create.html', {'form': form})


@check_session()
def view(request):
    label_id = request.GET.get('id')
    # content_id = request.GET.get['contentId']
    header = get_headers(request)
    label_data = requests.post(MIDDLEWARE_URL + "/content/label/get/"+label_id, headers=header)
    return render(request, 'label/view.html', {'labelData': json.loads(label_data.content.decode())})


@check_session()
def table_list(request):
    data = {
        "filters": json.loads(request.body)
    }
    # id = request.GET['id']
    header = get_headers(request)
    dataTableRow = requests.post(MIDDLEWARE_URL + "/content/label/list", data=json.dumps(data), headers=header)
    return JsonResponse(json.loads(dataTableRow.content.decode()))


@check_session()
def activate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if data['contentId,labelId']:
            header = get_headers(request)
            r_data = requests.post(MIDDLEWARE_URL + "/content/label/activate", data=json.dumps(data), headers=header)
            if r_data.status_code == 200:
                return HttpResponse()
            else:

                return HttpResponse(status=r_data.status_code)
        else:
            return HttpResponse(status=404)
