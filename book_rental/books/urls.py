from django.urls  import path, include
from . import views
from rest_framework.routers import DefaultRouter

from .views import BooksViewSet

router = DefaultRouter()
router.register(r'api/books', BooksViewSet)

urlpatterns = [
    path('books/', views.books, name='books'),
    path('books/details/<int:id>', views.details, name='details'),
    path('newbook/', views.newbook, name='newbook'),
    path('test/' , views.test, name='test'),
    path('', views.home, name='home'),

    path('', include(router.urls)), #Books API
]