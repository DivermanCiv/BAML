from django.http import HttpResponse
from django.shortcuts import render
import logging
from .utils import canonical_caseless
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

    This method catch the HTTP request from the Front End and return the
    content of the 404 page.

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with the 404 content.
    :rtype: HttpResponse
    """
    return render(request, 'BAML/404.html')


def html_500(request):
    """Method to redirect a 500 error to 500 page

    This method catch the HTTP request from the Front End and return the
    content of the 500.

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with the 500 page content.
    :rtype: HttpResponse
    """

    return render(request, 'BAML/500.html')


def how_we_work(request):
    """Method to go to the Qui Sommes Nous page

    This method catch the HTTP request from the Front End and return the
    content of the Qui Sommes nous page.

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with the Qui Sommes Nous page content.
    :rtype: HttpResponse
    """


    return render(request, 'BAML/qui-sommes-nous.html')


def legal_notices(request):

    """Method to present the legal mention page

        This method catch the HTTP request from the Front End and return the
        content of the legal_notices page.

        :param request: HTTP request
        :type request: HttpRequest
        :return: Response HTTP with legal notices page content.
        :rtype: HttpResponse
        """

    return render(request, 'BAML/mentions-legales.html')


def sitemap(request):
    """Method to go to the planDuSite page

        This method catch the HTTP request from the Front End and return the
        content of the site map page.

        :param request: HTTP request
        :type request: HttpRequest
        :return: Response HTTP with Sitemap page content.
        :rtype: HttpResponse
"""

    return render(request, 'BAML/plan-du-site.html')


def analyze(request, separator, csv_file=None):
    """Method to analyse the CVS file

    This method catch the HTTP request from the Front End and return the
    content of the analyse page.

    :param request : HTTP request.
    :type request: object
    :param separator: Separator in csv file.
    :type separator: str
    :param csv_file: CSV file uploaded.
    :type csv_file: object
    :return: A message displayed on analyse page.
    :rtype: str

    """

    message = "Vous avez choisi " + separator + " comme s??parateur de csv."
# todo: put the algorithm here.

    return message


def predict(request, separator, csv_file=None):
    """Method to predict the CSV file.

    This method catch the HTTP request from the frontend and return the content
    of the prediction page.

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


def bad_form_element(request, column, csvFile):

    """Method to check if there is an error in the csvfile received by the format

    Addressed errors :
        - selected column in the form match with an existing column in the file

        :param request : HTTP request.
        :param column : colum of the CVSFile.
        :param cvsFile : The cvsFile dropped.
        :return: an error message
        :rtype : str
    """
    error_message =""
    if column not in csvFile.fieldnames :
        error_message = "Le nom de colonne ?? analyser n'existe pas dans le fichier s??lectionn??"


    return error_message

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



def analyze_html(request):
    """Method to process the uploaded file when using the analyze function.

    This method catch the form response and check if there's an error in the file (cf bad_form_element()). If there is no error, it returns the analyzed file with the chosen separator, the column and the content of the csv file.
    If an error occurs, it returns a error page with an error type explanation.

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with analyze page content.
    :rtype: HttpResponse


    """
    if request.POST:

        separator = request.POST.get('separator')
        column = canonical_caseless(request.POST.get('column'))
        file = request.FILES['attachments[]']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file, delimiter = separator)

        error_message = bad_form_element(request, column, reader)

        for row in reader:
        # Get each cell value based on key-value pair.
        # Key will always be what lies on the first row.
            pass

        # analyse(request, separator, file)
        if error_message == "" :
            return render(request,
                      'BAML/analyse.html',
                      {
                              'separator': separator,
                               'column': column,
                               'csvFile' : decoded_file
                       })
        # , 'line_number' : line_number# })

        else :
            return render(request, 'BAML/erreur_formulaire.html',           {'error_message': error_message, 'previous': 'analyse'})

    else:
        return render(request, 'BAML/analyse.html')


def prediction_html(request):
    """Method to process the uploaded file when using the predict function.

    This method catch the form response and check if there's an error in the file (cf bad_form_element()). If there is no error, it returns the predicted file with the chosen separator, the column and the content of the csv file.
    If an error occurs, it returns a error page with an error type explanation.

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with prediction page content.
    :rtype: HttpResponse


    """
    if request.POST:

        separator = request.POST.get('separator')
        column = canonical_caseless(request.POST.get('column'))
        file = request.FILES['attachments[]']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        error_message = bad_form_element(request, column, reader)

        for row in reader:
            # Get each cell value based on key-value pair.
            # Key will always be what lies on the first row.
            pass

        # predict(request, separator, file)
        if error_message == "" :
            return render(request,
                      'BAML/prediction.html',
                      {
                              'separator': separator,
                               'column': column,
                               'csvFile' : decoded_file
                       })


        else :
            return render(request, 'BAML/erreur_formulaire.html',           {'error_message': error_message, 'previous': 'prediction'})

    else:
        return render(request, 'BAML/prediction.html')
