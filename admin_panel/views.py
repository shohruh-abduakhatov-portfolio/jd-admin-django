from django.shortcuts import render


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'admin_panel/login.html', {})
    if request.method == 'POST':
        pass


def profile(request):
    pass


def create(request):
    pass
