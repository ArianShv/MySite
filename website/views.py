from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse('dash *HTTP* test ba movaffaghiat anjam shod! \n میوووو')

def json_test(request):
    return JsonResponse({'res': 'mashi goloo inam az *json-test* boro berim'})

def home_views(request):
    return HttpResponse('Home Page')

def about_views(request):
    return HttpResponse('About Page')

def contact_views(request):
    return HttpResponse('Contact Page')

def main_views(request):
    return HttpResponse('Main Page! Welcome...')