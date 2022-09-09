from graphics import Matplotlib
from get_data import TXT

from string import digits

def main():
    t = TXT('data.txt')
    data = t.graphs_from_file()
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

            graph = Matplotlib((data[int(answer.strip()) - 1],))
            graph.draw_graphic()


        elif answer.strip() == '2':
            print(f'Какие графики отобразить? 1-{len(data)}')
            while True:
                print(f'Введите числа через пробел (1-{len(data)})')
                answer = input('> ')
                if len(answer.strip()) == 1:
                    print('Вы хотите отобразить один график?(yes or no)')
                    answer_1 = input('> ')
                    if answer_1.lower().startswith('y'):
                        graph = Matplotlib((data[int(answer.strip()) - 1],))
                        graph.draw_graphic()
                    else:
                        continue

                if all(i in n for i in answer.split()):
                    break
                else:
                    continue
            if len(answer.strip()) > 1:
                answer = [int(i) for i in answer.split()]
                send_data = [data[i - 1] for i in answer]
                graph = Matplotlib(send_data)
                graph.draw_graphic()
        else:
            continue

        print('Вы хотите повторить?( yes or no )')
        if not input('> ').lower().startswith('y'):
            break


if __name__ == '__main__':
    main()