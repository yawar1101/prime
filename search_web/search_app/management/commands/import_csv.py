import csv
import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings
from search_app.models import Restaurant

class Command(BaseCommand):
    help = 'Import data from csv'

    def handle(self, *args, **options):
        csv_file = os.path.join(settings.MEDIA_ROOT, 'csv', 'data.csv')
        dish_list = []

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    full_details = json.loads(row['full_details'])
                    items = json.loads(row['items'])
                    dish = Dish(
                        name=row['name'],
                        location=row['location'],
                        lat_long=row['lat_long'],
                        full_details=full_details,
                        items=items
                    )

                    dish_list.append(dish)
                except json.JSONDecodeError as e:
                    self.stderr.write(f'Error decoding JSON in row: {row}')
                    self.stderr.write(f'Error message: {str(e)}')

        Dish.objects.bulk_create(dish_list)

        self.stdout.write(self.style.SUCCESS('Data imported successfully!!!'))