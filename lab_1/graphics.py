from abc import ABC, abstractmethod

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# from get_data import TXT

# def graphs_from_file():
#     ''' ВЕРСИЯ С ВЫВОДОМ ИЗ ФАЙЛА ( сколько угодно графиков )'''
#     with open('data.txt') as f:
#         data = f.read()
#     data = data.split('\n')
#     new_data = []
#     for j in range(len(data)):
#         data_list = []
#         for i in data[j].split(','):
#             l = []
#             for sym in i.split():
#                 s = float(sym)
#                 l.append(s)
#             data_list.append(tuple(l))
#         new_data.append(tuple(data_list))
#     data = tuple(new_data)
#     return data

class Graphic(ABC):
    def __init__(self, points):
        self.points = points

    @abstractmethod
    def draw_graphic(self, points):
        pass

class Matplotlib(Graphic):
    def draw_graphic(self):
        data = self.points
        print(data[0])
        if len(data) == 1:
            x = [x[0] for x in data[0]]
            y = [x[1] for x in data[0]]

            print('Вывод точечного графика')
            plt.scatter(x, y)
            plt.show()

            print('Вывод графика')
            plt.plot(x, y)
            plt.show()
        else:
            for i in data:
                x = [x[0] for x in i]
                y = [x[1] for x in i]
                plt.scatter(x, y)
            print('Вывод точечных графиков')
            plt.show()

            for i in data:
                x = [x[0] for x in i]
                y = [x[1] for x in i]
                plt.plot(x, y)
            print('Вывод графиков')
            plt.show()

# t = TXT('data.txt')
# data = t.graphs_from_file()
# answer = input('> ')
# graph = Matplotlib((data[int(answer.strip()) - 1],))
# graph.draw_graphic()