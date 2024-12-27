from django.urls import path


from library.apps import LibraryConfig
from library.models import Author, Genre
from library.views import AuthorListAPIView, BookListAPIView, AuthorRetrieveAPIView, BookRetrieveAPIView, \
    AuthorCreateAPIView, BookCreateAPIView, OrderCreateAPIView, BookDestroyAPIView, AuthorDestroyAPIView, \
    AuthorUpdateAPIView, BookUpdateAPIView, OrderDestroyAPIView, OrderUpdateAPIView, OrderRetrieveAPIView, \
    OrderListAPIView, GenreCreateAPIView, GenreDestroyAPIView, OrderFinishPIView

app_name = LibraryConfig.name



urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(), name='author-list'),
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('author/<int:pk>', AuthorRetrieveAPIView.as_view(), name='author-one'),
    path('book/<int:pk>', BookRetrieveAPIView.as_view(), name='book-one'),
    path('author/create/', AuthorCreateAPIView.as_view(), name='author-create'),
    path('genre/create/', GenreCreateAPIView.as_view(), name='genre-create'),
    path('book/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('order/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('author/update/<int:pk>/', AuthorUpdateAPIView.as_view(), name='author-update'),
    path('book/update/<int:pk>/', BookUpdateAPIView.as_view(), name='book-update'),
    path('book/delete/<int:pk>/', BookDestroyAPIView.as_view(), name='book-delete'),
    path('genre/delete/<int:pk>/', GenreDestroyAPIView.as_view(), name='genre-delete'),
    path('author/delete/<int:pk>/', AuthorDestroyAPIView.as_view(), name='author-delete'),
    path('order/delete/<int:pk>/', OrderDestroyAPIView.as_view(), name='order-delete'),
    path('order/update/<int:pk>/', OrderUpdateAPIView.as_view(), name='order-update'),
    path('order/<int:pk>', OrderRetrieveAPIView.as_view(), name='order-one'),
    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('order/finish/<int:pk>/', OrderFinishPIView.as_view(), name='order-finish'),
]
