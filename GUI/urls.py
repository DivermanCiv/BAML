from django.conf.urls import url

from . import views # import views so we can use them in urls.


urlpatterns = [
    url(r'^analyzes$', views.analyze),
    url(r'^predictions$', views.predict)

]
