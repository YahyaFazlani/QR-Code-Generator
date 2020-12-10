from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pages.urls')),
    path('wifi-qr-code-generator/', include('WiFi_QR_Code_Generator.urls')),
    path('link-qr-generator/', include('Text_link_QR_Code_Generator.urls')),
]

handler404 = 'Pages.views.handler_404'
handler500 = 'Pages.views.handler_500'
handler400 = 'Pages.views.handler_400'
