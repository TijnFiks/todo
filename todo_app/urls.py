from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.list),
    path('new_list/', views.new_list),
    path('new_item/', views.new_item),
    path('delete_item/', views.delete_item),
    path('item/', views.item),
    path('delete_list/', views.delete_list),
]