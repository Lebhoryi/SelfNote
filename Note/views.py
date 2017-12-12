from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.




@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def editor(request):
    return render(request, 'mdEditor.html')


@login_required
def test(request):
    return render(request, 'test.md')