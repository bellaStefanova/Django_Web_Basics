from django.urls import path
from .views import ListBooksView, DetailBookView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', ListBooksView.as_view(), name='books'),
    path('books/<int:id>', DetailBookView.as_view()),
]
