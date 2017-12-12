from django import template

register = template.Library()

def jsontolist_path(path,level,folds):
    level = level + 1
    if isinstance(folds,dict):
        for fold,sub in folds.items():
            path.append((level,12-level,fold))
            jsontolist_path(path,level,sub)

    return path

@register.simple_tag
def deal_fold(folds):
    path = []
    level = 0
    return jsontolist_path(path,level,folds)


