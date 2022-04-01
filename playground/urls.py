from django.urls import URLPattern, path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.first_response)
]
