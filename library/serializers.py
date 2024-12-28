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
        fields = ('book', 'user',)

    def validate(self, data):
        book = data.get("book", None)
        user = data.get("user", None)
        if user:
            user_order = Order.objects.filter(user=user, is_returned=False).first()
            if user_order:
                raise serializers.ValidationError("Нельзя оформить заказ - у вас есть незавершенный заказ заказ")
        if book:
            book = Book.objects.filter(pk=book.pk).first()
            if book.quantity < 1:
                raise serializers.ValidationError("Нельзя оформить заказ - выданы все экземпляры книги")
        return data

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

