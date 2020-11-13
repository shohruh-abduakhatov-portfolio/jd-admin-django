from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from cms_panel.settings import DJANGO_URL


def get(request):
    # todo add IP check here
    user = authenticate(request)
    if user is None:
        url = DJANGO_URL
        token = request.GET.get('token')
        if token is not None:
            url += "?token=" + token
        return redirect(url)
    login(request, user)
    return redirect('/admin')
