from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="wifi_index"),
    path('result', result, name="wifi_result"),
]
