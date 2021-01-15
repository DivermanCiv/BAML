from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
import logging, traceback




# Create your views here.
def index(request):
    """Method to present the application HomePage

    This method catch the HTTP request from the Front End and return the
    content of the HomePage. This method also call the visitor_ip_address method which catch the user IP and send it to the log.

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with the HomePage content.
    :rtype: HttpResponse


    """

    return render(request, 'BAML/index.html')




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


def mentionLegales(request):

    """Method to present the legal mention page

        This method catch the HTTP request from the Front End and return the
        content of the Sitemap page.

        :param request: HTTP request
        :type request: HttpRequest
        :return: Response HTTP with Sitemap page content.
        :rtype: HttpResponse


        """

    return render(request, 'BAML/mention-legales.html')


def planDuSite(request):
    """Method to go to the planDuSite page"""

    return render(request, 'BAML/plan-du-site.html')



def analyze(request, separator, csvFile = None):
    """Method to analyse the CVS file

    This method catch the HTTP request from the Front End and return the
    content of the Sitemap page.

    :param string: separator
    :param file: csvFile
    :return: a message displayed on analyse page
    :rtype: string

    """

    message = "Vous avez choisi " + separator + " comme séparateur de CVS"


# mettre ici l'algorithme

    return message




def predict(request, separator, csvFile = None):
    """Method to prediction the CVS file

    This method catch the HTTP request from the Front End and return the
    content of the Sitemap page.

    :param string: separator
    :param file: csvFile
    :return: a message displayed on prediction page
    :rtype: string


    """
#mettre ici l'algorithme

    message = "Vous avez choisi " + separator + " comme séparateur de CVS"

    return message



def visitor_ip_address(request):
    """Method to get the user IP

    This method catch the user IP, throw it in IP.log and return it

    :param request: HTTP request
    :type request: HttpRequest
    :return: user IP adress
    :rtype: request


    """

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        logging.getLogger('django').info(ip)
    print(ip)
    return ip

def analyseHTML(request):
    separator = request.GET.get('separator')
    context = {'separator': separator}
    return render(request, 'BAML/analyse.html',context )

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

# def get_button_info(request):
#     if request.method == 'POST' and request.POST.get('buttonChoice'):
#         buttonChoice = request.POST.get('buttonChoice')
#
#         if buttonChoice == 'analyse' :
#             return 'analyse'
#
#         if buttonChoice == 'prediction':
#             return 'prediction'
