from ..models import *
from django.db.models import Count, Min


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    customers = Customer.objects.filter(order__date_formation__range=[begin, end]).annotate(
        order_count=Count('order'), order_before=Min('order__date_formation')
               ).values('name', 'order_count').order_by('-order_count', 'order_before', 'name').first()

    return (customers['name'], customers['order_count']) if customers else None
