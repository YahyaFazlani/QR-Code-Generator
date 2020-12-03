from re import template
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.defaults import bad_request, page_not_found, server_error, permission_denied
from base64 import b64encode
from io import BytesIO

from wifi_qrcode_generator import wifi_qrcode


def index(request):
  return render(request, "WiFi_QR_Code_Generator/index.html", status=405)


def result(request):
  # Form variables
  ssid = request.POST.get("ssid", None)
  print(ssid)
  if ssid == None:
    return render(request, "Error Pages/405.html", status=405)
  password = request.POST.get("password")
  encryption = request.POST.get("encryption")
  hidden = request.POST.get("hidden", default=False)
  if hidden == "on":
    hidden = True
  if encryption == "nopass":
    password = None

  qr_code = wifi_qrcode(
      ssid, hidden, encryption, password
  )

  # Converting image to base64
  output = BytesIO()
  qr_code.save(output, "PNG")
  image = output.getvalue()
  output.close()
  image = str(b64encode(image))[2:-1]

  # The context
  context = {
      'image': image
  }

  return render(request, "WiFi_QR_Code_Generator/result.html", context)


def handler_404(request, exception):
  return page_not_found(request, exception, template_name="Error Pages/404.html")


def handler_500(request):
  return server_error(request, template_name="Error Pages/500.html")
