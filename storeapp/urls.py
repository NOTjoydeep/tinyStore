from django.urls import URLPattern, path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_details)
]

