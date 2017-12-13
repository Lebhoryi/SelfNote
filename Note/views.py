from functools import reduce

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from os.path import split as path_split
from django.db.models import Q
import operator

import json
# Create your views here.

def get_path(fold):
    path = [fold.name]

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
    if request.is_ajax():    #show note list
        if 'path' in request.GET.keys():
            get = request.GET['path']
            local_path = request.session.get('path')
            folds=[]
            q_list=[]

            while len(get) > 1:    #可以用字符串拆分处理
                get, fold = path_split(get)
                folds.insert(0,fold)

            for path in folds:
                local_path=local_path[path]


            notes = local_path["YmFzZQ=="]
            for note in notes:
                q_list.append(Q(**{"id":note}))
            notes = Note.objects.filter(reduce(operator.or_, q_list))

        return render(request,"note_list.html",{"notes":notes})

    else:
        paths = []
        folds = {}
        fold_obj = Fold.objects.filter(user=request.user)

        for fold in fold_obj:
            notes = Note.objects.filter(fold__user=request.user, fold=fold)

            path = get_path(fold)
            tmp = folds
            while path:
                path_name = path.pop()
                if path_name not in tmp.keys():
                    tmp.update({path_name: {"YmFzZQ==":[]}})
                    for note in notes:
                        tmp[path_name]["YmFzZQ=="].append(note.id)
                tmp = tmp[path_name]

        request.session['path'] = folds
        return render(request, 'index.html',{"folds":folds})


@login_required
def editor(request):
    return render(request, 'mdEditor.html')


@login_required
def content(request):
    return render(request, 'test.md')