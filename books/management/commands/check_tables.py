# books/management/commands/check_tables.py
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Check the existence of specific tables'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            required_tables = [
                'books_author', 'books_category', 'books_publisher', 'books_book'
            ]
            for table in required_tables:
                if table in table_names:
                    self.stdout.write(self.style.SUCCESS(f'Table "{table}" exists.'))
                else:
                    self.stdout.write(self.style.ERROR(f'Table "{table}" does not exist.'))