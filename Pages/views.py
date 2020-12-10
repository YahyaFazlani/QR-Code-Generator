from django.shortcuts import render
from django.views.defaults import bad_request, page_not_found, server_error


def index(request):
  return render(request, "Pages/index.html")


def google_file(request):
  return render(request, "google5c02155bdaa39045.html")


def handler_404(request, exception):
  return page_not_found(request, exception, template_name="Error Pages/404.html")


def handler_500(request):
  return server_error(request, template_name="Error Pages/500.html")


def handler_400(request, exception):
  return bad_request(request, exception, template_name="Error Pages/400.html")
