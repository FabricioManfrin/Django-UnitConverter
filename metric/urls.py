from django.urls import path

from . import views

urlpatterns = [
    path('', views.length_converter, name='length-converter'),
    path('temperature/', views.temperature_converter, name='temperature-converter')

]
