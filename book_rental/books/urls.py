from django.urls  import path
from . import views

urlpatterns = [
    path('books/', views.books, name='books'),
    path('books/details/<int:id>', views.details, name='details'),
    path('newbook/', views.newbook, name='newbook'),
    path('test/' , views.test, name='test'),
    path('', views.home, name='home')
]