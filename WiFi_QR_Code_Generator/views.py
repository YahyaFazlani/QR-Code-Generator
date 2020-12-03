from django.shortcuts import render
from django.views.generic.base import TemplateView


def index(request):
  return render(request, "WiFi_QR_Code_Generator/index.html")

class ResultView(TemplateView):
  template_name = "WiFi_QR_Code_Generator/result.html"
