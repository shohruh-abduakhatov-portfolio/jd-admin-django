import json

import requests
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render

from login.forms import LoginUserForm
from railwayadmin.settings import MIDDLEWARE_URL, API_HEADERS
from utils.helpers import is_loged_in, get_headers


@is_loged_in()
def auth(request):
    if request.method == 'POST':
        header = get_headers(request)
        print(">>> auth POST")
        form = LoginUserForm(request.POST)
        if form.is_valid():
            if validate_recapture(request):
                try:
                    response = requests.post(MIDDLEWARE_URL + "/users/login", data=json.dumps(form.as_dict()),
                                             headers=header)
                    assert response.status_code == 200 or response.ok, Exception
                    token = json.loads(response.content.decode()).get('token')
                    request.session['token'] = token
                    request.session.set_expiry(900)
                except Exception:
                    messages.error(request, 'Error')
                return HttpResponseRedirect('/user')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

    else:
        print(">>> auth Index")
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})


def validate_recapture(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    verify_rs = requests.get(url, params=values, verify=True)
    verify_rs = verify_rs.json()
    status = verify_rs.get("success", False)
    return status


@is_loged_in()
def logout(request):
    header = get_headers(request)
    response = requests.post(MIDDLEWARE_URL + "/users/logout", headers=header)
    body = json.loads(response.content.decode())
    if body is None or body is False:
        return HttpResponseServerError()
    request.session.flush()
    return HttpResponseRedirect('/')
