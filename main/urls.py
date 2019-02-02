from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_category', views.add_cat),
    path('admin/', views.admin, name='admin2'),
    path('admin/catalog/', views.admin, name='admin2'),
    path('admin/system/', views.admin, name='admin2'),
]