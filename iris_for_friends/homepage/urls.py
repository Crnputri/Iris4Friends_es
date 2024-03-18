from django.urls import path

from . import views

app_name = 'página de inicio'

urlpatterns = [
    path('', views.index, name='index'),
]
