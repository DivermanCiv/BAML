"""BAML URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from BAML import settings
from GUI import views

urlpatterns = [
    url(r'^$', views.index),
    url('application/', views.application,),
    url('mention-legales/', views.mentionLegales),
    url('plan-du-site/', views.planDuSite),
    url('qui-sommes-nous/', views.quiSommesNous),
    path('admin/', admin.site.urls),
    #url('analyze/', views.application, name="analyze"),
    url('prediction/', views.predictionHTML, name ="predictionHTML"),
    path('analyze', views.analyseHTML, name="analyzeHTML")


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
