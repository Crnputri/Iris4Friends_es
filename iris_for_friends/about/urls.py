from django.urls import path

from . import views

app_name = 'acerca de'

urlpatterns = [
    path('', views.description, name='descripción'),
]
