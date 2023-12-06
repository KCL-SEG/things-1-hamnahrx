from django.shortcuts import render

def home(request):
    html = "<html><head><title>Things</title><body><h1>Things</h1></body></head></html>"
    return HttpResponse(html)