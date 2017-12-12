from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def get_path(fold):
    path = [fold.name]
    level = 0
    while fold.parent is not None:
        path.append(fold.parent.name)
        fold = fold.parent

    return path

def create_path(paths):
    fold = {}
    for path in paths:
        tmp = fold
        while path:
            path_name = path.pop()
            if path_name not in tmp.keys():
                tmp.update( { path_name:{} } )
            tmp = tmp[path_name]

    return fold




@login_required
def index(request):

    if request.is_ajax():
        pass

    paths = []
    fold_obj = Fold.objects.filter(user=request.user)
    for fold in fold_obj:
        paths.append(get_path(fold))

    folds=create_path(paths)

    return render(request, 'index.html',{"folds":folds})


@login_required
def editor(request):
    return render(request, 'mdEditor.html')


@login_required
def content(request):
    return render(request, 'test.md')