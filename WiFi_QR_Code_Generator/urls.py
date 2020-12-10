from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="wifiQR_index"),
    path('result', result, name="wifiQR_result"),
]
