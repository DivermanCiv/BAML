from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def index(request):
    """Method to present the application HomePage

    This method catch the HTTP request from the Front End and return the
    content of the HomePage.

    :param request: HTTP request
    :type request: HttpRequest
    :return: Response HTTP with the HomePage content.
    :rtype: HttpResponse

    .. todo: Tests unitaire
    .. todo: contenu à revoir
    """
    return render(request, 'BAML/index.html')


def application(request):
    """Method to go to the application page"""

    return render(request, 'BAML/application.html')

def analyse(request):
    message = "Analyse des données"
    return HttpResponse(message)


def predict(request):
    message = "Prédiction des données"
    return HttpResponse(message)
