from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from library.models import Author, Book, Order, Genre
from library.paginators import LibraryPaginator
from library.serializers import AuthorSerializer, BookSerializer, OrderSerializer, \
    GenreSerializer, OrderCreateSerializer
from users.permissions import UserIsModeratorPermission, UserIsStaffPermission, IsOwnerPermission


class GenreCreateAPIView(generics.CreateAPIView):
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated, UserIsModeratorPermission | UserIsStaffPermission]

class GenreDestroyAPIView(generics.DestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | UserIsModeratorPermission]


class AuthorDestroyAPIView(generics.DestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | UserIsModeratorPermission]


class AuthorCreateAPIView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, UserIsModeratorPermission | UserIsStaffPermission]


class AuthorListAPIView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    pagination_class = LibraryPaginator
    permission_classes = [IsAuthenticated,]


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated,]


class AuthorUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | UserIsModeratorPermission]


class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, UserIsModeratorPermission | UserIsStaffPermission]


class BookDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | UserIsModeratorPermission]


class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [SearchFilter,]
    search_fields = ['name', 'author', 'genre']
    pagination_class = LibraryPaginator
    permission_classes = [IsAuthenticated, ]


class BookRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, ]


class BookUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | UserIsModeratorPermission]


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        order = serializer.save()
        if not order.user:
            order.user = self.request.user
        order.book.quantity -= 1
        order.book.save()
        order.save()


class OrderUpdateAPIView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | UserIsModeratorPermission]


class OrderFinishPIView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | UserIsModeratorPermission]

    def perform_update(self, serializer):
        order = serializer.save(is_returned=True)
        order.book.quantity += 1
        order.book.save()
        super().perform_update(order)


class OrderRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerPermission | UserIsStaffPermission | UserIsModeratorPermission]


class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    pagination_class = LibraryPaginator
    permission_classes = [IsAuthenticated, UserIsStaffPermission | UserIsModeratorPermission]


class OrderDestroyAPIView(generics.DestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, UserIsStaffPermission | UserIsModeratorPermission]
