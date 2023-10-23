from decimal import Decimal
from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    pure_profit = serializers.SerializerMethodField("get_pure_profit")

    class Meta:
        model = Book
        fields = '__all__'

    def get_pure_profit(self, obj):
        profit_percentage = Decimal('0.60')
        pure_profit = obj.price * profit_percentage
        return pure_profit

class AuthorSerializer(serializers.ModelSerializer):
    
    books = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Author
        fields = '__all__'
