class Multiplier:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Multiplier(self.value + other.value)

    def __sub__(self, other):
        return Multiplier(self.value - other.value)

    def __truediv__(self, other):
        return Multiplier(self.value / other.value)

    def __mul__(self, other):
        return Multiplier(self.value * other.value)

    def get_value(self) -> int:
        return self.value


class Hundred(Multiplier):
    """Множитель на 100"""
    def __init__(self, value):
        super().__init__(value)
        self.value = value * 100


class Thousand(Multiplier):
    """Множитель на 1 000"""
    def __init__(self, value):
        super().__init__(value)
        self.value = value * 1000


class Million(Multiplier):
    """Множитель на 1 000 000"""

    def __init__(self, value):
        super().__init__(value)
        self.value = value * 1000000



