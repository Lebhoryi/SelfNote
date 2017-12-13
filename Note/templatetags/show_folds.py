from django import template

register = template.Library()

def jsontolist_path(paths,level,folds,path):
    level = level + 1

    if isinstance(folds,dict):
        for fold,sub in folds.items():
            if fold == "YmFzZQ==":
                pass
            else:
                paths.append((level,12-level,fold, path+'/' +fold))
                jsontolist_path(paths,level,sub, path+'/' +fold)

    return paths

@register.simple_tag
def deal_fold(folds):
    path = ""
    paths = []
    level = 0
    return jsontolist_path(paths,level,folds,path)


