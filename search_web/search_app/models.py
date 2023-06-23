from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=150, default='name')
    location = models.CharField(max_length=60, default='dummy')
    items = models.JSONField(default=list)
    lat_long = models.CharField(max_length=50, default='0.0')
    full_details = models.JSONField(default=list)

    def __str__(self):
        return self.name 

    def set_full_details(self, full_details):
        self.full_details = full_details
    
    def get_full_details(self):
        return self.full_details

    def set_items(self, items):
        self.items = items
    
    def get_items(self):
        return self.items
