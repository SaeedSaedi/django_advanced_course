from django.http import HttpResponse
from django.shortcuts import render
from .tasks import sendEmail


# Create your views here.
def send_mail(request):
    sendEmail.delay()
    return HttpResponse("email sent")
