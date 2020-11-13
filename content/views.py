import json

import requests
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.

from railwayadmin.settings import MIDDLEWARE_URL, API_HEADERS
from content.forms import CreateContentForm
from utils.helpers import check_session


@check_session()
def index(request):
    return render(request, 'content/index.html', {})


@check_session()
def create(request):
    header = API_HEADERS
    # header['Authorization'] = "Bearer {}".format(request.session['token'])
    if request.method == 'POST':
        content_id = request.POST['identifier']
        form = CreateContentForm(request.POST)
        if form.is_valid():
            if content_id:
                requests.post(MIDDLEWARE_URL + "/content/edit", data=json.dumps(form.as_dict(True)), headers=header)
            else:
                requests.post(MIDDLEWARE_URL + "/content/create", data=json.dumps(form.as_dict()), headers=header)
            return HttpResponseRedirect('/content')
    else:
        form = CreateContentForm()

    content_id = request.GET.get('id')
    if content_id:
        content = requests.post(MIDDLEWARE_URL + "/content/get/"+content_id, headers=header)
        form = CreateContentForm(json.loads(content.content.decode()))
    return render(request, 'content/create.html', {'form': form})


@check_session()
def view(request):
    content_id = request.GET.get('id')
    header = API_HEADERS
    # header['Authorization'] = "Bearer {}".format(request.session['token'])
    content_data = requests.post(MIDDLEWARE_URL + "/content/get/"+content_id, headers=header)
    return render(request, 'content/view.html', {'contentData': json.loads(content_data.content.decode())})


@check_session()
def table_list(request):
    data = {
        "filters": json.loads(request.body)
    }
    header = API_HEADERS
    # header['Authorization'] = "Bearer {}".format(request.session['token'])
    dataTableRow = requests.post(MIDDLEWARE_URL + "/content/list", data=json.dumps(data), headers=header)
    return JsonResponse(json.loads(dataTableRow.content.decode()))


@check_session()
def table_list(request):
    data = {
        "filters": json.loads(request.body)
    }
    header = API_HEADERS
    # header['Authorization'] = "Bearer {}".format(request.session['token'])
    dataTableRow = requests.post(MIDDLEWARE_URL + "/content/list", data=json.dumps(data), headers=header)
    return JsonResponse(json.loads(dataTableRow.content.decode()))


@check_session()
def activate(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        if data['contentId']:
            header = API_HEADERS
            # header['Authorization'] = "Bearer {}".format(request.session['token'])
            r_data = requests.post(MIDDLEWARE_URL + "/content/activate", data=json.dumps(data), headers=header)
            if r_data.status_code == 200:
                return HttpResponse()
            else:

                return HttpResponse(status=r_data.status_code)
        else:
            return HttpResponse(status=404)
