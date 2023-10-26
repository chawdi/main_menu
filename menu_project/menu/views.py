from django.shortcuts import render, get_object_or_404
from .models import MenuItem



def menu_list(request):
    current_url = request.path
    menu_root_items = MenuItem.objects.filter(parent=None)

    has_active_children = {}
    for item in menu_root_items:
        has_active_children[item.id] = item.children.filter(url=current_url).exists()

    return render(request, 'menu/list.html', {
        'menu_root_items': menu_root_items,
        'current_url': current_url,
        'has_active_children': has_active_children
    })


def menu_item_view(request, named_url):
    current_item = get_object_or_404(MenuItem, named_url=named_url)
    menu_root_items = MenuItem.objects.filter(parent=None)
    child_items = current_item.children.all()
    ancestors = current_item.get_ancestors()
    has_active_grandchildren = {}

    for child in current_item.children.all():
        has_active_grandchildren[child.id] = child.has_children()

    context = {
        'current_item': current_item,
        'menu_root_items': menu_root_items,
        'ancestors': ancestors,
        'has_active_grandchildren': has_active_grandchildren
    }

    return render(request, 'menu_template.html', context)