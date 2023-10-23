from django.urls import path
from . import views


urlpatterns = [
    path('list', views.book_list, name='book_list'),
    path('add', views.add_book, name='add_book'),
    path('update/<int:book_id>', views.update_book, name='update_book'),
    path('delete/<int:book_id>', views.delete_book, name='delete_book'),
    path('borrow/<int:book_id>', views.borrow, name='borrow'),
    path('priceUpdate/<int:book_id>', views.update_price, name='update_price'),
    path('byAuthor/', views.books_by_author, name='books_by_author'),
    path('createAuthor', views.create_author, name='create-author'),
    path('booksByAuthor/<int:author_id>', views.books_by_author, name='books-by-author')
]
