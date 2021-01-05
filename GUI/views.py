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
   
        
    return render(request, 'BAML/index.html')


"""Method to present the application page

    This method catch the HTTP request from the Front End and return the
    content of the application page. 
    If the form is fill, the page will be redirected on the user choice

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with application page content.
    :rtype: HttpResponse
    

    """

def application(request):
    """Method to go to the application page"""
#TODO ajouter parametre au redirect
    getChoice = get_form_info(request)

    if getChoice == 'analyze':
        radioChoice = request.POST.get('algoChoice')
        separator = request.POST.get('separator')
        csvFile = request.POST.get('csvFile')
        return redirect('analyzeHTML', permanent=True)

    if getChoice == 'prediction':
        radioChoice = request.POST.get('algoChoice')
        separator = request.POST.get('separator')
        csvFile = request.POST.get('csvFile')
        return redirect('predictionHTML')


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


"""Method to analyse the CVS file

    This method catch the HTTP request from the Front End and return the
    content of the Sitemap page. 

    :param string: separator
    :param file: csvFile
    :return: a message displayed on analyse page
    :rtype: string
    

    """

def analyze(request, separator, csvFile = None):
    message = "Vous avez choisis " + separator + " comme séparateur de CVS"


# mettre ici l'algorythme

    return message


    """Method to prediction the CVS file

    This method catch the HTTP request from the Front End and return the
    content of the Sitemap page. 

    :param string: separator
    :param file: csvFile
    :return: a message displayed on prediction page
    :rtype: string
    

    """

def predict(request, separator, csvFile = None):

#mettre ici l'algorythme
    return message


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

def analyseHTML(request, separator=';'):

    return render(request, 'BAML/analyse.html', {'separator': separator})

def predictionHTML(request, separator=';'):
    return render(request, 'BAML/prediction.html',{'separator': separator} )


def get_form_info(request):
    if request.method == 'POST' and request.POST.get('algoChoice'):
            radioChoice = request.POST.get('algoChoice')
            separator = request.POST.get('separator')
            csvFile = request.POST.get('csvFile')

            if radioChoice == 'analyze':
              
                return 'analyze'

            if radioChoice == 'prediction':
                return 'prediction'
