from tasks.common import MyException


class Value:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __truediv__(self, other):
        if other == 0:
            raise MyException
        else:
            return self.value / other

    def __mul__(self, other):
        return self.value * other
