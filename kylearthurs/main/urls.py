from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('dev', views.dev, name='dev'),
        path('business-finance', views.business_finance, name='business-finance'),
        path('philosophy-philanthropy', views.philosophy_philanthropy, name='philosophy-philanthropy'),
        path('collections', views.collections, name='collections'),
]