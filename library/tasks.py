from datetime import datetime

from celery import shared_task

from library.services import send_telegram_message
from library.models import Order

@shared_task
def send_telegram_notification():
    today = datetime.now().astimezone()
    orders = Order.objects.filter(is_returned=False)
    for order in orders:
         if (order.return_at - today).days < 2:
            message = f"Завтра пора вернуть книгу {order.book}"
            send_telegram_message(order.user.t_chat_id, message)


@shared_task
def clean_orders():
    Order.objects.filter(is_returned=True).delete()

