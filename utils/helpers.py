from functools import wraps

from django.http import HttpResponseRedirect
from django.shortcuts import render

from cms_panel.cms_panel.settings import API_HEADERS
from login.forms import LoginUserForm
from railwayadmin.settings import SESSION_EXP


def check_session():
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            request = args[0]
            try:
                request.session['token']
                return f(*args, **kwargs)
            except KeyError:
                form = LoginUserForm()
                return render(request, 'login.html', {'form': form})


        return wrapped


    return decorator


def is_loged_in():
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            request = args[0]
            token = request.session.get('token')
            if token is None:
                token = request.GET.get('token')
            if token is not None and request.path is "/":
                request.session['token'] = token
                request.session.set_expiry(SESSION_EXP)
                return HttpResponseRedirect('/user')

            return f(*args, **kwargs)


        return wrapped


    return decorator

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_headers(request):
    header = API_HEADERS
    header['Authorization'] = "Bearer {}".format(request.session.get('token'))
    header['X-FORWARDED-FOR'] = get_client_ip(request)
    header['User-Agent'] = request.META['HTTP_USER_AGENT']
    return header
