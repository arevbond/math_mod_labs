'''
 Задание номер 1
Вывод простейшего поточечного графика
'''
import matplotlib.pyplot as plt
from string import digits


def write_data():
    '''
    Функция для работы с вводом данных из консоли
    '''
    print('Необходимо ввести не менее 5-ти пар вещественных точек (x,y) ')
    print('Отделять коориданту x от y ПРОБЕЛОМ')
    print('Координаты отделять ЗАПЯТОЙ')
    print('Пример ввода: 1 1, 2 2, 3.4 5, 6.7 9, 10 2')
    while True:
        data = input('Введите данные > ')
        data = data.strip()
        if len(data.split(',')) < 5:
            print('Введите не менее 5-ти пар вещественных точек (x,y)')

        correct_symbols = digits + ' ,'
        data_list = []
        try:
            for i in data.split(','):
                if len(i.split()) != 2:
                    print('Введите кооректные даныне')
                    break
                l = []
                for sym in i.split():
                    s = float(sym)
                    l.append(s)
                data_list.append(l)
            break
        except ValueError:
            print('Введите корректные данные')
            continue
    data = tuple(tuple(i) for i in data_list)
    print('Ваши данные : ', data)
    return data


def show_graph(data):
    '''
    Функция отображает график ( один или несколько ) на экран
    '''
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


def graphs_from_console():
    ''' ВЕРСИЯ С ВЫВОДОМ ИЗ ТЕРМИНАЛА ( только 1 график )'''
    while True:
        data = write_data()
        show_graph((data,))

        print('Хотите повторить ещё раз (yes or no)')
        if not input('> ').lower().startswith('y'):
            break


def graphs_from_file():
    ''' ВЕРСИЯ С ВЫВОДОМ ИЗ ФАЙЛА ( сколько угодно графиков )'''
    with open('data.txt') as f:
        data = f.read()
    data = data.split('\n')
    new_data = []
    for j in range(len(data)):
        data_list = []
        for i in data[j].split(','):
            l = []
            for sym in i.split():
                s = float(sym)
                l.append(s)
            data_list.append(tuple(l))
        new_data.append(tuple(data_list))
    data = tuple(new_data)
    print(f'На вход подано {len(data)} набора точек')

    n = list(digits[1:len(data) + 1])

    while True:
        print('Сколько графиков отобразить? (1 - один) (2 - несколько)')
        print('Введите значение 1 либо 2')
        answer = input('> ')
        if answer.strip() == '1':
            while True:
                print(f'Какой график отобразить? 1-{len(data)}')
                answer = input('> ')
                if len(answer.strip()) != 1 or answer.strip() not in n:
                    print('Введите корректное значение')
                    continue
                else:
                    break
            show_graph((data[int(answer.strip()) - 1],))


        elif answer.strip() == '2':
            print(f'Какие графики отобразить? 1-{len(data)}')
            while True:
                print(f'Введите числа через пробел (1-{len(data)})')
                answer = input('> ')
                if len(answer.strip()) == 1:
                    print('Вы хотите отобразить один график?(yes or no)')
                    answer_1 = input('> ')
                    if answer_1.lower().startswith('y'):
                        show_graph((data[int(answer.strip()) - 1],))
                    else:
                        continue

                if all(i in n for i in answer.split()):
                    break
                else:
                    continue
            if len(answer.strip()) > 1:
                answer = [int(i) for i in answer.split()]
                send_data = [data[i - 1] for i in answer]
                show_graph(send_data)
        else:
            continue

        print('Вы хотите повторить?( yes or no )')
        if not input('> ').lower().startswith('y'):
            break


if __name__ == '__main__':
    graphs_from_file()
