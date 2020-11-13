from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from cms_panel.cms_panel.settings import CMS_URL
from utils.helpers import check_session


# Create your views here.


@check_session()
def index(request):
    return HttpResponseRedirect(CMS_URL + "?token="+request.session.get('token'))


@check_session()
def to_admin(request):
    return HttpResponseRedirect(CMS_URL + "auth?token="+request.session.get('token'))

