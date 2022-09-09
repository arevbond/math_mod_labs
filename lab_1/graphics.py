from abc import ABC, abstractmethod

from matplotlib import pyplot as plt


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
            data = sorted(data[0])
            x = [x[0] for x in data]
            y = [x[1] for x in data]

            print('Вывод точечного графика')
            plt.scatter(x, y)
            plt.show()

            print('Вывод графика')
            plt.plot(x, y)
            plt.show()
        else:
            for i in data:
                points = sorted(i)
                x = [x[0] for x in points]
                y = [x[1] for x in points]
                plt.scatter(x, y)
            print('Вывод точечных графиков')
            plt.show()

            for i in data:
                points = sorted(i)
                x = [x[0] for x in points]
                y = [x[1] for x in points]
                plt.plot(x, y)
            print('Вывод графиков')
            plt.show()
