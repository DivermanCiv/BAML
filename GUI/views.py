from django.http import HttpResponse
from django.shortcuts import render
import logging
from .utils import canonical_caseless
# import traceback
import csv


# Create your views here.
def index(request):
    """Method to present the application HomePage

    This method catch the HTTP request from the Front End and return the
    content of the HomePage. This method also call the visitor_ip_address
    method which catch the user IP and send it to the log.

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with the HomePage content.
    :rtype: HttpResponse
    """
    visitor_ip_address(request)
    print(request.build_absolute_uri())

    return render(request, 'BAML/index.html')


def html_404(request, exception):
    """Method to redirect a 404 error to 404 page

    """
    return render(request, 'BAML/404.html')


def html_500(request):
    """Method to redirect a 500 error to 500 page

    """

    return render(request, 'BAML/500.html')


def how_we_work(request):
    """Method to go to the Qui Sommes Nous page"""

    return render(request, 'BAML/qui-sommes-nous.html')


def legal_notices(request):

    """Method to present the legal mention page

        This method catch the HTTP request from the Front End and return the
        content of the Sitemap page.

        :param request: HTTP request
        :type request: HttpRequest
        :return: Response HTTP with Sitemap page content.
        :rtype: HttpResponse


        """

    return render(request, 'BAML/mentions-legales.html')


def sitemap(request):
    """Method to go to the planDuSite page"""

    return render(request, 'BAML/plan-du-site.html')


def analyze(request, separator, csv_file=None):
    """Method to analyse the CVS file

    This method catch the HTTP request from the Front End and return the
    content of the Sitemap page.

    :param request : HTTP request.
    :type request: object
    :param separator: Separator in csv file.
    :type separator: str
    :param csv_file: CSV file uploaded.
    :type csv_file: object
    :return: A message displayed on analyse page.
    :rtype: str

    """

    message = "Vous avez choisi " + separator + " comme séparateur de csv."


# todo: put the algorithm here.

    return message


def predict(request, separator, csv_file=None):
    """Method to predict the CSV file.

    This method catch the HTTP request from the frontend and return the content
    of the Sitemap page.

    :param request : HTTP request.
    :type request: object
    :param separator : Delimiter of the csv file.
    :type separator: str
    :param csvFile : CSV file uploaded.
    :type csv_file: object
    :return: A message displayed on prediction page.
    :rtype: str
    """
    #  Mettre ici l'algorithme

    with open(csv_file):
        csv_reader = csv.reader(csv_file, delimiter=separator)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Les noms de colonnes sont {separator.join(row)}')
                line_count += 1
            else:
                line_count += 1
        line_number = line_count - 1

    return line_number


# def bad_form_element(request, separator, column, csvFile):

#     separator = request.POST.get('separator')
#     column = request.POST.get('column')
#     file = request.FILES['attachments[]']

#     with open(csvFile):
#         csv_reader = csv_reader(csvFile, delimiter=separator)
#         line_count = 0
#         try:
#             for row in csv_reader:
#                 if line_count == 0:
#                    if not (column )

#     return

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
    return ip

# def createLog(request, csv_lines=None, duration=None, analyze_number=None):
# 	ip = visitor_ip_address(request)
# 	current_url = request.build_absolute_uri()


def analyze_html(request):
    if request.POST:

        separator = request.POST.get('separator')
        column = canonical_caseless(request.POST.get('column'))
        file = request.FILES['attachments[]']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
        # Get each cell value based on key-value pair.
        # Key will always be what lies on the first row.
            print(row)

        # analyse(request, separator, file)
        return render(request,
                      'BAML/analyse.html',
                      {
                              'separator': separator,
                               'column': column,
                               'csvFile' : decoded_file
                       })
        # , 'line_number' : line_number# })

    else:
        return render(request, 'BAML/analyse.html')


def prediction_html(request):
    if request.POST:

        separator = request.POST.get('separator')
        column = canonical_caseless(request.POST.get('column'))
        file = request.FILES['attachments[]']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            # Get each cell value based on key-value pair.
            # Key will always be what lies on the first row.
            print(row)

        # predict(request, separator, file)
        return render(request,
                      'BAML/prediction.html',
                      {
                              'separator': separator,
                              'column': column,
                              'csvFile': decoded_file
                      })
        # , 'line_number' : line_number# })

    else:
        return render(request, 'BAML/prediction.html')

# def createLog(request, csv_lines=None, duration=None, analyze_number=None):
#     ip = visitor_ip_address(request)
#     current_url = request.build_absolute_uri()
#
#     file = open(request.data[2])
#     reader = csv.reader(file)
#     lines = len( list(reader))
