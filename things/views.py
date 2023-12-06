from django.http import HttpResponse

def home(request):
    html = "<html><head><title>Things</title><body><h1>Things</h1></body></head></html>"
    return HttpResponse(html)