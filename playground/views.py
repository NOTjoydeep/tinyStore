from itertools import product
from turtle import title
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction, connection
from django.db.models import DecimalField, Q, F, Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.contrib.contenttypes.models import ContentType
from storeapp.models import Product, Customer, Collection, Order, OrderItem, Cart, CartItem
from tags.models import TaggedItem

# Create your views here.
# turns requests -> response
# request handler
# action

def first_response(request):
    # every model has an attribute 'object', which returns a manager, an interface to DB
    # manager has few methods to modify a query. all(), get(), count
    #query_set = Product.objects.all() # returns a query set.

    # # django translates the query set while iterating, or while converting in to list
    # # or while indexing or silcing
    # for product in query_set:
    #     print(product)
    # list(query_set)
    # query_set[0:5]
    # query_set[0]

    # we can modify query set without executing the query. we can add multiple filters too.
    # query_set.filter().filter().order_by()
    # try:
    #     product = Product.objects.get(pk=1)

    # except ObjectDoesNotExist:
    #     print("Primary key does not exist.")

    # __gt, __gte as prefix for GREATER THAN
    # __lt, __lte as prefix for LOWER THAN
    # query_set = Product.objects.filter(unit_price__gte=20)
    # query_set = Product.objects.filter(unit_price__range=(20, 40))

    # with "__" we can navigate in relationship, like collection id below
    # query_set = Product.objects.filter(collection__id__range=(1,2,3))

    # query_set = Product.objects.filter(title__contains='coffee') # __contains is case sesitive
    # query_set = Product.objects.filter(title__icontains='coffee') # __icontains is not case sensitive
    # has __startswith, __istartswith, __endswith, __iendswith
    # query_set = Customer.objects.filter(email__iendswith='.com')
    # query_set = Collection.objects.filter(featured_product__isnull=True)
    # query_set = Product.objects.filter(inventory__lt=10)
    # query_set = Order.objects.filter(customer__id=1)
    # query_set = OrderItem.objects.filter(product__collection__id=3) # order items for products in collection 3
    
    # # Multiple filters. Product quantity <10 OR price < 20
    # query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # # Multiple filters. Product quantity <10 OR price < 20 (Q used with bitwise operator)
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    # F object used to send a variable as a unitvalue for keyword argument
    # query_set = Product.objects.filter(inventory=F('unit_price')) # WHERE inventory == unit price
    # query_set = Product.objects.filter(inventory=F('collection__id')) # also can be used with different tables

    # query_set = Product.objects.order_by('title') # default order by
    
    # query_set = Product.objects.order_by('unit_price', '-title').reverse()
    # order by unitprice, then reverse order by title, then reverse the whole order

    # # product = Product.objects.order_by('unit_price')[0] # we are fetching only first element from here
    # product = Product.objects.earliest('unit_price') # similarly .latest() for the last object
    # return render(request, 'hello.html', {'name' : 'LAZY', 'product' : product})

    # # products = Product.objects.all()[:5] # objects with id 0,1,2,3,4
    # products = Product.objects.all()[5:10] # objects with id 5,6,7,8,9
    # return render(request, 'hello.html', {'name' : 'LAZY', 'products' : products})

    # # values used to search only in he specific fields. 
    # products = Product.objects.values('id', 'title', 'collection__title')
    # return render(request, 'hello.html', {'name' : 'LAZY', 'products' : products})

    # # query_set = Product.objects.filter(id=F('orderitem__product_id')).order_by('title').distinct()
    # query_set = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')
    # return render(request, 'hello.html', {'name' : 'LAZY', 'products' : list(query_set)})

    # select_related helps us specifically pick the related table,
    # otherwise, the product table makes an individual quary for all the collection entities
    # slowing the page down while it waits for the query to return.
    # select_related used when the other end of the relation has one instance,
    # like product has one collection
    # prefetch_related used when other end of relation has many objects,
    # like promotions of a product.(manytomany field)
        # products = Product.objects.select_related('collection').all()
    # products = Product.objects.prefetch_related('promotions').all()

    # # to get all the promotioned products with collections
    # products = Product.objects.prefetch_related('promotions').select_related('collection').all()
    # return render(request, 'hello.html', {'name' : 'LAZY', 'products' : products})

    # # result_dict = Product.objects.aggregate(Count('id'))
    # result_dict = Product.objects.filter(collection_id=3).aggregate(Max('unit_price'), Min('unit_price'), Avg('unit_price'))
    # return render(request, 'hello.html', {'name' : 'LAZY', 'result' : result_dict})

    # Annotation example
    # query_set = Customer.objects.annotate(is_new=Value(True))
    # query_set = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    # query_set = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name'))
    # return render(request, 'hello.html', {'name' : 'LAZY', 'query_set' : list(query_set)})

    # Number of orders a customer has create
    # query_set = Customer.objects.annotate(order_count=Count('order'))
    # return render(request, 'hello.html', {'name' : 'LAZY', 'query_set' : list(query_set)})

    # # discounted price (expression wrapper)
    # discounded_price_expression = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # query_set = Product.objects.annotate(discounted_price = discounded_price_expression)
    # return render(request, 'hello.html', {'name' : 'LAZY', 'query_set' : list(query_set)})

    # # Customers with their last order id
    # query_set = Customer.objects.annotate(last_order=Max('order__id'))
    # return render(request, 'hello.html', {'name' : 'LAZY', 'query_set' : list(query_set)})

    # # collections and counts of their products
    # query_set = Collection.objects.annotate(product_count=Count('product'))
    # return render(request, 'hello.html', {'name' : 'LAZY', 'query_set' : list(query_set)})

    # # customers with more than 5 orders
    # query_set = Customer.objects.annotate(order_count = Count('order')).filter(order_count__gte=5)
    # return render(request, 'hello.html', {'name' : 'LAZY', 'query_set' : list(query_set)})

    # # customers and the total amount they spent
    # query_set = Customer.objects.annotate(
    #     total_expense = Sum(F('order__orderitem__unit_price')*F('order__orderitem__quantity')))
    # return render(request, 'hello.html', {'name' : 'LAZY', 'query_set' : list(query_set)})

    # # top 5 best selling products and heir total sales.
    # query_set = Product.objects.annotate(
    #     total_sale=Sum(F('orderitem__unit_price')*F('orderitem__quantity'))).order_by(
    #         '-total_sale')[:5]
    # return render(request, 'hello.html', {'name' : 'LAZY', 'query_set' : list(query_set)})

    # Addding tags to from tags app to products.
    # content_type = ContentType.objects.get_for_model(Product)
    # query_set = TaggedItem.objects\
    #             .select_related('tag')\
    #             .filter(
    #                 content_type=content_type,
    #                 object_id=1
    #             )
    # The object_id above will be dynamic and will replace depending on which product is being browsed
    # return render(request, 'hello.html', {'name' : 'LAZY', 'tags' : list(query_set)})
    # BETTER method is to modify the 'objcts' manager accordingly(inheritance)
    # query_set = TaggedItem.objects.get_tags_for(Product, 1) # '1' is product id, will be dynamic by default
    # return render(request, 'hello.html', {'name' : 'LAZY', 'tags' : list(query_set)})

    # # Insert into a table.
    # collection = Collection()
    # collection.title = 'Video Game'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    # # collection.id
    # return render(request, 'hello.html', {'name' : 'LAZY'})

    # # Update data from table
    # # collection = Collection.objects.get(title='Video Game')
    # # collection.title = 'Game'
    # # collection.save()
    # # OR
    # Collection.objects.filter(title='Game').update(title='Video Game')

    # # Delete data from table
    # collection = Collection(title='Video Game')
    # collection.delete()
    # # Collection.objects.filter(id__gte=5).delete()
    # return render(request, 'hello.html', {'name' : 'LAZY'})

    # # Create a shopping cart with an item
    # cart = Cart()
    # cart.save()

    # item = CartItem()
    # item.quantity = 2
    # item.cart = cart
    # item.product_id = 1
    # item.save()
    # return render(request, 'hello.html', {'name' : 'LAZY'})

    # # Update quantity of the shopping cart
    # item = CartItem.objects.get(id=1)
    # item.quantity = 1
    # item.save()
    # return render(request, 'hello.html', {'name' : 'LAZY'})

    # orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # return render(request, 'hello.html', {'name' : 'LAZY', 'orders' : orders})

    # # TRANSACTIONS
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    # return render(request, 'hello.html', {'name' : 'LAZY', 'items' : item})

    # Raw Query
    # raw_query = Product.objects.raw("SELET * FROM store_product")
    with connection.cursor() as cursor:
        cursor.execute("SELET * FROM store_product")
    # always close cursor.close()

    return render(request, 'hello.html', {'name' : 'LAZY', 'result' : list(raw_query)})

    # return HttpResponse('First Request processed.')
    # return render(request, 'hello.html', {'name' : 'LAZY', 'customers' : list(query_set)})
    # return render(request, 'hello.html', {'name' : 'LAZY', 'collections' : list(query_set)})
    # return render(request, 'hello.html', {'name' : 'LAZY', 'products' : list(query_set)})
    # return render(request, 'hello.html', {'name' : 'LAZY', 'orders' : list(query_set)})
    # return render(request, 'hello.html', {'name' : 'LAZY', 'orderitems' : list(query_set)})
    # return render(request, 'hello.html', {'name' : 'LAZY', 'products' : list(query_set)})

# @transaction.atomic()
# def first_response(request):
#     # TRANSACTIONS
#     order = Order()
#     order.customer_id = 1
#     order.save()

#     item = OrderItem()
#     item.order = order
#     item.product_id = 1
#     item.quantity = 1
#     item.unit_price = 10
#     item.save()

#     return render(request, 'hello.html', {'name' : 'LAZY', 'orders' : order})

