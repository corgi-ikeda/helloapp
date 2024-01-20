from django.shortcuts import render
from django.http import HttpResponse

def hellofunction(request):
    return render(request, 'helloworldapp/hello.html')
    #return HttpResponse('Hello world!')

