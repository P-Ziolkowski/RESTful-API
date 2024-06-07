from django.db import models

class Product(models.Model):
    name = models.CharField("nazwa", max_length=255)
    description = models.TextField("opis")
    price = models.DecimalField("cena", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("ilosc dostepnych sztuk")
    category = models.CharField("kategoria", max_length=255)
    date_added = models.DateTimeField("data dodania", auto_now_add=True)
    # Django will automatically add a field to hold the primary key


    def __str__(self):
        return self.name