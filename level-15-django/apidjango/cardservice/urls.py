from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='card-service-index'),
    path('show/<id>', views.show, name='card-service-show'),
    path('create', views.create, name='card-service-create'),
    path('update/<id>', views.update, name='card-service-update'),
    path('delete/<id>', views.delete, name='card-service-delete'),
]