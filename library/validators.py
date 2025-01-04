from rest_framework import serializers
from library.models import Order, Book


class UserValidator:

    def __call__(self, order):
        if order:
            user = order.get("user")
            user_order = Order.objects.filter(user=user.pk, is_returned=False).first()
            if user_order:
                raise serializers.ValidationError("Нельзя оформить заказ - у вас есть незавершенный заказ")

class BookValidator:

    def __call__(self, order):
        if order:
            book = order.get("book")
            if book.quantity < 1:
                raise serializers.ValidationError("Нельзя оформить заказ - выданы все экземпляры книги")