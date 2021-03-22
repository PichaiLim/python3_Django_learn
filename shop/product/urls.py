""" 
    urls product app
"""

from django.urls import path
from .views import Home, Aboutme, Mobile

urlpatterns = [
    path('', view=Home, name='home-product'),
    path('about/', view=Aboutme, name='about-me'),
    path('mobile/', view=Mobile, name='mobile-product'),
]
