from django.db import models
from django.core.exceptions import ValidationError

def validate_non_negative(value):
    if value < 0:
        raise ValidationError("Price cannot be negative.")

class Author(models.Model):
    name = models.CharField(max_length=255)
    author_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_non_negative])
    book_id = models.IntegerField(primary_key=True)
    borrow_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
