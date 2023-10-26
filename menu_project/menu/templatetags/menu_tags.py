from django import template
from ..models import MenuItem
from django.contrib.sites.models import Site
from django.template.loader import render_to_string

register = template.Library()


@register.filter(name='get_active_children')
def get_active_children(value, arg):
    return value.get(arg, False)


@register.simple_tag
def draw_menu(menu_name):
    root_items = MenuItem.objects.filter(menu_name=menu_name, parent=None)
    return render_to_string('menu/draw_menu.html', {'menu_root_items': root_items})