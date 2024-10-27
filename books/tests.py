from django.test import TestCase #It's the base class for all the tests you'll write. It provides useful testing tools, like setting up test data and checking if your code behaves correctly.
from rest_framework.test import APIClient #APIClient is a tool from Django REST Framework that lets you simulate API requests like GET, POST, and others.
from .models import Author, Book, Category, Publisher

class BookstoreAPITests(TestCase):
    
    def setUp(self):  # This sets up the test environment before each test
        self.client = APIClient()  # Initializes the API client for making requests

        # Create a category for the book
        self.category = Category.objects.create(name='Science')

        # Create an author for the book
        self.author = Author.objects.create(name='Hawking, Stephen W')

        # Create a publisher for the book
        self.publisher = Publisher.objects.create(name='Bantam Books')

        # Create a book, linking it to the category, author, and publisher
        self.book = Book.objects.create(
            title='A Brief History of Time',
            author=self.author,
            category=self.category,  # <-- Make sure the book has a category
            publisher=self.publisher,  # <-- Also, make sure the book has a publisher
            price_starting_with=4.29,
            publish_date_month='March',
            publish_date_year=1988
        )
    def test_list_books(self): #This is one of the tests. It checks if your API can correctly list all the books when someone makes a GET request to /api/books/.
        response = self.client.get('/api/books/') #Makes a GET request to the /api/books/ endpoint.
        self.assertEqual(response.status_code, 200) #Checks if the API returns an HTTP 200 status code, meaning everything is OK.
        self.assertGreater(len(response.data), 0) # Checks if the API returns at least one book (i.e., the response data is not empty).


    def test_search_books_by_author(self): #This test checks if your API can filter books by author name.
        response = self.client.get('/api/books/?author__name=Hawking') #Sends a request to search for books where the author’s name contains "Hawking".
        self.assertEqual(response.status_code, 200) #Verifies that the request was successful (status code 200).
        self.assertEqual(response.data[0]['title'], 'A Brief History of Time') #Ensures that the first book returned has the correct title ("A Brief History of Time").
