from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# turns requests -> response
# request handler
# action

def foobar():
    foo = 'bar'
    return foo

def first_response(request):
    # return HttpResponse('First Request processed.')
    foo = foobar()
    return render(request, 'hello.html', {'name' : 'LAZY'})
