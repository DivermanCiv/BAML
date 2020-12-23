from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
import logging, traceback




# Create your views here.
def index(request):
    """Method to present the application HomePage

    This method catch the HTTP request from the Front End and return the
    content of the HomePage. This method also call the visitor_ip_address method which catch the user IP and send it to the log

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with the HomePage content.
    :rtype: HttpResponse
    

    """
    visitor_ip_address(request)
    return render(request, 'BAML/index.html')


"""Method to present the application page

    This method catch the HTTP request from the Front End and return the
    content of the application page. 

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with application page content.
    :rtype: HttpResponse
    

    """

def application(request):
    """Method to go to the application page"""
    get_form_info(request)

    return render(request, 'BAML/application.html')


"""Method to present the team page

    This method catch the HTTP request from the Front End and return the
    content of the team page. 

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with team page content.
    :rtype: HttpResponse
    

    """
def quiSommesNous(request):
    """Method to go to the Qui Sommes Nous page"""

    return render(request, 'BAML/qui-sommes-nous.html')


"""Method to present the legal mention page

    This method catch the HTTP request from the Front End and return the
    content of the legal mention page. 

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with legal mention page content.
    :rtype: HttpResponse
    

    """
def mentionLegales(request):
    """Method to go to the Sitemap page"""

    return render(request, 'BAML/mention-legales.html')


"""Method to present the legal mention page

    This method catch the HTTP request from the Front End and return the
    content of the Sitemap page. 

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with Sitemap page content.
    :rtype: HttpResponse
    

    """
def planDuSite(request):
    """Method to go to the planDuSite page"""

    return render(request, 'BAML/plan-du-site.html')

def analyze(request):
    #message = "Analyse des données"
    #pass
    return render(request, 'BAML/analyse.html')

    #return HttpResponse(message)


def predict(request):
    message = "Prédiction des données"
    #return HttpResponse(message)
    return render(request, 'BAML/analyse.html')


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
    print(ip)
    return ip


def get_form_info(request):


    if request.method == 'POST':
        radioChoice = request.POST.get('algoChoice')
        separator = request.POST.get('separator')
        csvFile = request.POST.get('csvFile')

        if radioChoice == 'analyze':
            print('je suis une ' + radioChoice + ' mon séparateur est ' + separator + " et je contiens " + csvFile.name)
            return HttpResponseRedirect('analyze/')

        if radioChoice == 'prediction':
            print('je suis une ' + radioChoice + ' mon séparateur est ' + separator + " et je contiens " + csvFile.name)
            return redirect('/prediction/')
    
                