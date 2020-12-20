from django.urls import include, path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('dev', views.dev, name='dev'),
        path('collections/', include('main.collections.urls')),
        path('business-finance', views.business_finance, name='business-finance'),
        path('philosophy', views.philosophy, name='philosophy'),
        path('blog', views.blog, name='blog'),
]