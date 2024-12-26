from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .tasks import sendEmail
import requests


# Create your views here.
def send_mail(request):
    sendEmail.delay()
    return HttpResponse("email sent")


@cache_page(60)
def test(request):
    # if not cache.get("test_delay"):
    response = requests.get(
        "https://f131de9d-a934-4741-a533-c2b9332eee16.mock.pstmn.io/test/5"
    )
    # cache.set("test_delay", response.json(), 30)
    # return JsonResponse(cache.get("test_delay"))
    return JsonResponse(response.json())
