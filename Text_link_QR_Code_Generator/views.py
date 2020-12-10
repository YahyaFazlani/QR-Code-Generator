from io import BytesIO
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render
import pyqrcode
from base64 import b64encode


def index(request):
  return render(request, "Text_link_QR_Code_Generator/index.html")


def result(request):
  link = request.POST.get("link", None)
  if link == None:
    raise SuspiciousOperation
  qr_code = pyqrcode.create(link)

  output = BytesIO()
  qr_code.png(output, scale=11)
  image = output.getvalue()
  output.close()
  image = str(b64encode(image))[2:-1]

  context = {
      'image': image
  }

  return render(request, "Text_link_QR_Code_Generator/result.html", context)
