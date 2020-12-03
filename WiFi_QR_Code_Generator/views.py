from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "WiFi_QR_Code_Generator/index.html")