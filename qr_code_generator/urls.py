from django.conf.urls import handler403
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wifi-qr-code-generator/', include('WiFi_QR_Code_Generator.urls'))
]

handler404 = 'WiFi_QR_Code_Generator.views.handler_404'
handler500 = 'WiFi_QR_Code_Generator.views.handler_500'
