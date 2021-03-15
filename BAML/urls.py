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
# from django.contrib import admin
from django.urls import path, include

import debug_toolbar

from BAML import settings
from GUI import views

handler404 = 'GUI.views.html_404'
handler500 = 'GUI.views.html_500'

urlpatterns = [
    url(r'^$', views.index),
    url('mentions-legales/', views.legal_notices),
    url('plan-du-site/', views.sitemap),
    url('qui-sommes-nous/', views.how_we_work),
    # path('admin/', admin.site.urls),
    url('prediction/', views.prediction_html, name="predictionHTML"),
    url(r'analyse/$', views.analyze_html, name="analyzeHTML")
]

if settings.DEBUG:
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
