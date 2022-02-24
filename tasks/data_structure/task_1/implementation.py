class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """
    def __init__(self, *args):
        self.values = args

    def __getitem__(self, item):
        return self.values[item]

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.

        Args:
            value: количество вхождений в объекте
        """
        count = 0
        for element in self.values:
            if element == value:
                count += 1

        return count

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.

        Args:
            value: индекс искомого элемента
        """

        if value not in self.values:
            raise ValueError

        for index, item in enumerate(self.values):
            if item == value:

                return index
