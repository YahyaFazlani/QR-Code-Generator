from django.shortcuts import render
from django.views.defaults import bad_request, page_not_found, server_error
from base64 import b64encode
from django.core.exceptions import SuspiciousOperation
from io import BytesIO

from wifi_qrcode_generator import wifi_qrcode


def index(request):
  # raise SuspiciousOperation
  return render(request, "WiFi_QR_Code_Generator/index.html", status=405)


def result(request):
  # Form variables
  ssid = request.POST.get("ssid", None)
  if ssid == None:
    raise SuspiciousOperation
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


def handler_400(request, exception):
  return bad_request(request, exception, template_name="Error Pages/400.html")
