from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Author, Category, Publisher, Book
from .serializer import AuthorSerializer, BookSerializer, CategorySerializer, PublisherSerializer

# Author Views
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorSearchByName(APIView):
    def get(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        if name:
            authors = Author.objects.filter(name__icontains=name)
            serializer = AuthorSerializer(authors, many=True)
            return Response(serializer.data)
        return Response({"error": "Name not provided"}, status=400)

# Book Views
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookSearchByCategory(APIView):
    def get(self, request, *args, **kwargs):
        category_name = request.query_params.get('category')
        if category_name:
            try:
                category = Category.objects.get(name__iexact=category_name)
                books = Book.objects.filter(category=category)
                serializer = BookSerializer(books, many=True)
                return Response(serializer.data)
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=404)
        return Response({"error": "Category name not provided"}, status=400)

class BookSearchByAuthor(APIView):
    def get(self, request, *args, **kwargs):
        author_name = request.query_params.get('author')
        if author_name:
            try:
                author = Author.objects.get(name__icontains=author_name)
                books = Book.objects.filter(author=author)
                serializer = BookSerializer(books, many=True)
                return Response(serializer.data)
            except Author.DoesNotExist:
                return Response({"error": "Author not found"}, status=404)
        return Response({"error": "Author name not provided"}, status=400)

# Category Views
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Publisher Views
class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer