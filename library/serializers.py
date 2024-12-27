from rest_framework import serializers
from rest_framework.serializers import ValidationError


from library.models import Book, Author, Order, Genre


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'book',)

    def validate(self, data):
        book = data.get("book", None)
        if book:
            book = Book.objects.filter(pk=book.pk).first()
            if book.quantity < 1:
                raise serializers.ValidationError("Нельзя оформить заказ - выданы все экземпляры книги")
        return data

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderFinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('user', 'book', 'started_at', 'return_at', 'is_returned')