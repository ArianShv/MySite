from django.urls import path
from website.views import *

urlpatterns = [
    path('http-test', http_test),
    path('json-test', json_test),
    path('', main_views),
    path('home', home_views),
    path('about', about_views),
    path('contact', contact_views)


]