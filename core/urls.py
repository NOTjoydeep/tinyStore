from django.views.generic import TemplateView
from django.urls import URLPattern, path

# URLConf
urlpatterns = [
    path('', TemplateView.as_view(template_name = 'core/index.html'))
]
