from django.urls import path
from website.views import *
app_name = 'website'


urlpatterns = [
    path('http-test', http_test, name= 'http_test'),
    path('json-test', json_test, name= 'json-test'),
    #path('', main_views),
    path('index', index_views, name= 'index'),
    path('', index_views),
    path('about', about_views, name = 'about'),
    path('contact', contact_views, name= 'contact')


]