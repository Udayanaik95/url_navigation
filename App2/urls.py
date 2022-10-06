from django.urls import URLPattern, path
from App2.views import *
app_name='App2'

urlpatterns=[
    path('Sthird/',Sthird,name='Sthird'),
]