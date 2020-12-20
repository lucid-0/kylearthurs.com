from django.urls import include, path
from . import views

urlpatterns = [
        path('', views.collections, name='collections'),
        path('books', views.books, name='books'),
        path('records', views.records, name='records'),
        path('games', views.games, name='games'),
]