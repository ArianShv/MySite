from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse('dash *HTTP* test ba movaffaghiat anjam shod! \n میوووو')

def json_test(request):
    return JsonResponse({'res': 'mashi goloo inam az *json-test* boro berim'})

def index_views(request):
    return render(request,'website/index.html')

def about_views(request):
    return render(request, 'website/About.html')

def contact_views(request):
    return render(request, 'website/contact.html')

def main_views(request):
    return HttpResponse('Main Page! Welcome...')