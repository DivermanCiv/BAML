from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import logging, traceback



# Create your views here.
def index(request):
    """Method to present the application HomePage

    This method catch the HTTP request from the Front End and return the
    content of the HomePage.

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with the HomePage content.
    :rtype: HttpResponse
    

    """
    visitor_ip_address(request)
    return render(request, 'BAML/index.html')


def application(request):
    """Method to go to the application page"""

    return render(request, 'BAML/application.html')

def quiSommesNous(request):
    """Method to go to the Qui Sommes Nous page"""

    return render(request, 'BAML/qui-sommes-nous.html')

def mentionLegales(request):
    """Method to go to the mentionsLegales page"""

    return render(request, 'BAML/mention-legales.html')

def planDuSite(request):
    """Method to go to the planDuSite page"""

    return render(request, 'BAML/plan-du-site.html')

def analyse(request):
    message = "Analyse des données"
    return HttpResponse(message)


def predict(request):
    message = "Prédiction des données"
    return HttpResponse(message)



    """Method to get the user IP

    This method catch the user IP, throw it in IP.log and return it

    :param request: HTTP request
    :type request: HttpRequest
    :return: user IP adress
    :rtype: request
    

    """
def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        logging.getLogger('django').info(ip)
    
    return ip
