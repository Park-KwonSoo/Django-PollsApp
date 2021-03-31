from django.http import HttpResponse

def index(request) :
    return HttpResponse('Hello, World! Im in at the polls index.')

def testing(request) :
    return HttpResponse('Hi, I am Kwonsoo Park')

# Create your views here.
