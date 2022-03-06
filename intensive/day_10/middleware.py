import json
import time
import sys

from django.http import HttpResponse
from django.http import JsonResponse

from django.utils.deprecation import (
    MiddlewareMixin,
)


class StatisticMiddleware:
    """
    Компонент вычисляющий время выполнения запроса на сервере и размер ответа в байтах.
    Отображает значения в консоли приложения
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        total = (time.time() - start_time) * 1000
        print(f'Продолжительность запроса {request.path} - {total} сек.')
        print(f'Размер ответа: {sys.getsizeof(response)} байт')
        return response


class FormatterMiddleware:
    """
    Компонент форматирующий Json ответ в HttpResponse
    {'key': value} => <p>key = value</p>
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if type(response) is JsonResponse:
            new_data = ''
            content = json.loads(response.content)
            for key, value in content.items():
                new_data += f'<p>{key} = {value}</p>'
            response = HttpResponse(new_data)

        return response


class CheckErrorMiddleware(MiddlewareMixin):
    """
        Перехватывает необработанное исключение в представлении и отображает ошибку в виде
        "Ошибка: {exception}"
    """

    @staticmethod
    def process_exception(request, exception):
        message = HttpResponse(f'Ошибка: {exception}')
        return message



