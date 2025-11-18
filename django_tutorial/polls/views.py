from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,world yout're at the polls index")