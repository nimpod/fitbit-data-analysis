class FitbitDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def toMDYWithSlash(self):
        return '{}/{}/{}'.format(self.month, self.day, self.year[2:])

    def toYMDWithHyphen(self):
        return '{}-{}-{}'.format(self.year, self.month, self.day)
