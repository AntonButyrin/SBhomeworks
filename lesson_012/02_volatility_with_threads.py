# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import os
from threading import Thread


class StockParser(Thread):

    def __init__(self, openfile, tickerzero, tickerdata, *args, **kwargs, ):
        super().__init__(*args, **kwargs, )
        self.file = openfile
        self.vol = None
        self.count = None
        self.tickers_zero = tickerzero
        self.tickers_data = tickerdata

    def run(self):
        with open(self.file) as ff:
            self.operations(ff)
        if self.vol == 0:
            self.tickers_zero.append(self.count)
        else:
            self.tickers_data[self.count] = self.vol

    def operations(self, ff):
        next(ff)
        a = next(ff)
        self.count, tradetime, price, quantity = a.split(",")
        maxi = float(price)
        mini = float(price)
        for a in ff:
            self.count, tradetime, price, quantity = a.split(",")
            int_price = float(price)
            if mini > int_price:
                mini = int_price
            elif maxi < int_price:
                maxi = int_price
        self.computing(mini, maxi)

    def computing(self, mini, maxi):
        try:
            middle = (mini + maxi) / 2
            self.vol = ((maxi - mini) / middle) * 100
        except TypeError:
            print("Error")


def main():
    tickers_data = {}
    tickers_zero = []
    all_flows = []
    for dirp, i, filename in os.walk("trades"):
        for file in filename:
            path = os.path.join(dirp, file)
            process = StockParser(path, tickerdata=tickers_data, tickerzero=tickers_zero)
            all_flows.append(process)

    for i in all_flows:
        i.start()

    for i in all_flows:
        i.join()

    print("Максимальная волатильность:")
    print(dict(sorted(tickers_data.items(), key=lambda x: x[1], reverse=True)[:3]))
    print("Минимальная волатильность:")
    print(dict(sorted(tickers_data.items(), key=lambda x: x[1])[:3]))
    print("Нулевая волантильность:")
    print(tickers_zero)


if __name__ == '__main__':
    main()

# Зачёт!
