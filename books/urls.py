from django.urls import path
from .views import (
    AuthorList,
    AuthorDetail,
    BookList,
    BookDetail,
    CategoryList,
    CategoryDetail,
    PublisherList,
    PublisherDetail,
    AuthorSearchByName,
    BookSearchByCategory,
    BookSearchByAuthor,
)

urlpatterns = [
    # Author endpoints
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('authors/search/', AuthorSearchByName.as_view(), name='author-search'),

    # Book endpoints
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/search/category/', BookSearchByCategory.as_view(), name='book-search-category'),
    path('books/search/author/', BookSearchByAuthor.as_view(), name='book-search-author'),

    # Category endpoints
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    # Publisher endpoints
    path('publishers/', PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherDetail.as_view(), name='publisher-detail'),
]