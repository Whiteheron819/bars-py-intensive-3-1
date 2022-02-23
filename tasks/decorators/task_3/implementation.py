count = 0


def counter(func):
    """
    Обертка для подсчёта количества вызовов обернутой функции.

    Returns:
        int - количество вызовов функции.
    """

    def wrapper():
        global count
        count += 1
        return count
    return wrapper
