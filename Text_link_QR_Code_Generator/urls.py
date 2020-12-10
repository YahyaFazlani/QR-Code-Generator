from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="linkQR_index"),
    path('result', result, name="linkQR_result")
]
