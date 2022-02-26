import datetime as dt


class MathClock:

    def __init__(self):
        """
        Задаём начальное время
        """
        self.time = dt.datetime.strptime('00:00', '%H:%M')

    def __add__(self, other):
        """
        Функция увеличения количества минут, работающая при сложении с int
        """
        self.time += dt.timedelta(minutes=other)

    def __sub__(self, other):
        """
        Функция уменьшения количества минут, работающая при вычитании с int
        """
        self.time -= dt.timedelta(minutes=other)

    def __mul__(self, other):
        """
        Функция увеличения количества часов, работающая при умножении на int
        """
        self.time += dt.timedelta(hours=other)

    def __truediv__(self, other):
        """
        Функция уменьшения количества часов, работающая при делении на int
        """
        self.time -= dt.timedelta(hours=other)

    def get_time(self):
        return self.time.strftime('%H:%M')
