from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
import logging, traceback, csv




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


def html404(request, exception):
    """Method to redirect a 404 error to 404 page

    """

    return render(request, 'BAML/404.html')


def html500(request):
    """Method to redirect a 500 error to 500 page

    """

    return render(request, 'BAML/500.html')


def quiSommesNous(request):
    """Method to go to the Qui Sommes Nous page"""

    return render(request, 'BAML/qui-sommes-nous.html')


def mentionsLegales(request):

    """Method to present the legal mention page

        This method catch the HTTP request from the Front End and return the
        content of the Sitemap page.

        :param request: HTTP request
        :type request: HttpRequest
        :return: Response HTTP with Sitemap page content.
        :rtype: HttpResponse


        """

    return render(request, 'BAML/mentions-legales.html')


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

    with open(csvFile) :
        csv_reader = csv_reader(csvFile, delimiter = separator)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Les noms de colonnes sont {separator.join(row)}')
                line_count += 1
            else :
                line_count += 1
        line_number = line_count - 1

    return line_number



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
    if request.POST :

        separator = request.POST.get('separator')
        file = request.FILES['attachments[]']

        if not file.name.endswith('.csv'):
            print("error")
            return(render(request, 'BAML/analyse.html'))

        # predict(request, separator, file)
        return render(request, 'BAML/analyse.html',{'separator': separator, 'csvFile' : file}) #, 'line_number' : line_number# })

    else :
        return(render(request, 'BAML/prediction.html'))


def predictionHTML(request):
    if request.POST :

        separator = request.POST.get('separator')
        file = request.FILES['attachments[]']

        if not file.name.endswith('.csv'):
            print("error")
            return(render(request, 'BAML/prediction.html'))

        # predict(request, separator, file)
        return render(request, 'BAML/prediction.html',{'separator': separator, 'csvFile' : file}) #, 'line_number' : line_number# })

    else :
        return(render(request, 'BAML/prediction.html'))




#def createLog(request, csv_lines=None, duration=None, analyze_number=None):
# ip = visitor_ip_address(request)
# current_url = request.build_absolute_uri()
#
# file = open(request.data[2])
# reader = csv.reader(file)
# lines = len( list(reader))
