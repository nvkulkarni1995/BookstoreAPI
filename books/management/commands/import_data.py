import pandas as pd
from django.core.management.base import BaseCommand
from books.models import Author, Category, Publisher, Book

class Command(BaseCommand):
    help = 'Import data from Excel files'

    def handle(self, *args, **kwargs):
        try:
            # Import Authors
            authors_df = pd.read_excel('C:/Users/neha1/Documents/author_500_clean.xlsx')
            for _, row in authors_df.iterrows():
                Author.objects.get_or_create(name=row['Author_name'])
            print("Authors imported successfully")

            # Import Categories
            categories_df = pd.read_excel('C:/Users/neha1/Documents/category_books_500.xlsx')
            for _, row in categories_df.iterrows():
                Category.objects.get_or_create(name=row['Category_name'])
            print("Categories imported successfully")

            # Import Publishers
            publishers_df = pd.read_excel('C:/Users/neha1/Documents/publisher_500_clean.xlsx')
            for _, row in publishers_df.iterrows():
                Publisher.objects.get_or_create(name=row['Publisher_name'])
            print("Publishers imported successfully")

            # Import Books
            books_df = pd.read_excel('C:/Users/neha1/Documents/book_500_clean.xlsx')
            for _, row in books_df.iterrows():
                author = Author.objects.get(name=row['Authors'])
                category = Category.objects.get(name=row['Category'])
                publisher = Publisher.objects.get(name=row['Publisher'])
                Book.objects.get_or_create(
                    title=row['Title'],
                    author=author,
                    category=category,
                    publisher=publisher,
                    price_starting_with=row['Price Starting With ($)'],
                    publish_date_month=row['Publish Date-Month'],
                    publish_date_year=row['Publish Date-Year']
                )
            print("Books imported successfully")

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        
        except Exception as e:
            print(f"An error occurred: {e}")