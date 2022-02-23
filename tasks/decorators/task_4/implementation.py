import time

from tasks.common import MyException


def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            for second in range(1, times + 1, 1):
                try:
                    result = func(*args, **kwargs)
                    if result is not None:

                        return result
                except AssertionError:
                    if second == times:
                        raise MyException
                    time.sleep(delay)

        return wrapper

    return real_decorator
