from django.shortcuts import render
from django.http import HttpResponse
from storeapp.models import Product

# Create your views here.
# turns requests -> response
# request handler
# action

def first_response(request):
    # every model has an attribute 'object', which returns a manager, an interface to DB
    # manager has few methods to modify a query. all(), get(), count()
    query_set = Product.objects.all() # returns a query set.

    # # django translates the query set while iterating, or while converting in to list
    # # or while indexing or silcing
    # for product in query_set:
    #     print(product)
    # list(query_set)
    # query_set[0:5]
    # query_set[0]

    # we can modify query set without executing the query. we can add multiple filters too.
    query_set.filter().filter().order_by()


    # return HttpResponse('First Request processed.')
    return render(request, 'hello.html', {'name' : 'LAZY'})
