class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitors


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32
