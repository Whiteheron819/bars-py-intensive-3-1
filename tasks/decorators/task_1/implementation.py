import time
from tasks.common import factorial


def time_execution(func):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции: {execution_time} с.')

        return result

    return wrapper


@time_execution
def my_function(value):
    return factorial(value)


print(my_function(100000))
