from tasks.common import MyException


def check_value(func):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(*args, **kwargs):

        for arg in args:
            if type(arg) != int or arg < 0:
                raise MyException
        result = func(*args, **kwargs)
        return result

    return wrapper

