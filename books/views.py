from django.shortcuts import get_object_or_404
from books.models import Book, Author
from books.serializers import BookSerializer, AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_book(request):
    data = request.data
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT'])
def update_book(request, book_id):
    data = request.data
    book = get_object_or_404(Book, book_id=book_id)
    serializer = BookSerializer(book, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response("Update book successfully")
    return Response("Cannot update book, the object is not in the correct format")

@api_view(['DELETE'])
def delete_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    book.delete()
    return Response({'message': 'Book deleted successfully'})

@api_view(['PUT'])
def borrow(request, book_id):
    data = request.data
    field_name = "borrow_status"
    new_value = data.get("borrow_status")
    book = get_object_or_404(Book, pk=book_id)
    if hasattr(book, field_name):
        setattr(book, field_name, new_value)
        book.save()
        return Response(f"Updated {field_name} successfully")
    return Response(f"Field {field_name} does not exist in the book model.")

@api_view(['GET'])
def books_by_author(request):
    author = request.query_params.get('author')
    if author:
        author = get_object_or_404(Author, name=author)
        books = Book.objects.filter(author=author)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response("Please provide an 'author' query parameter.", status=400)

@api_view(['PUT'])
def update_price(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)
    data = request.data
    serializer = BookSerializer(book, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def books_by_author(request, author_id):
    author = get_object_or_404(Author, author_id=author_id)
    books = Book.objects.filter(author=author)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
