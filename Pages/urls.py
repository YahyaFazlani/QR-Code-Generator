from django.urls import path

from .views import index, google_file, sitemap

urlpatterns = [
  path('', index),
  path('google5c02155bdaa39045.html', google_file),
  path('sitemap.xml', sitemap)
]
