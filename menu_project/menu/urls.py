from django.urls import path
from . import views


app_name = 'menu'

urlpatterns = [
    path('list/', views.menu_list, name='menu_list'),
    path('list/<str:named_url>/', views.menu_item_view, name='menu_item_view'),
]

