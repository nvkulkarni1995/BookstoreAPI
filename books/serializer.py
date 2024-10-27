from rest_framework import serializers
from .models import Author, Category, Publisher, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'publisher', 'price_starting_with', 'publish_date_month', 'publish_date_year']

    # Add validation for title and author
    def validate_title(self, value):                                #validate_title: Ensures that the book title is provided. If not, it raises an error.
        if not value:
            raise serializers.ValidationError("Title is required.")
        return value

    def validate_author(self, value):                               #validate_author: Ensures that the author is provided. If not, it raises an error.

        if not value:
            raise serializers.ValidationError("Author is required.")
        return value
    
