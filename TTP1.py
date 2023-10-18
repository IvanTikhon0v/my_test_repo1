import math
import random
import os


def calculate(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def find(points):
    max_distance = 0
    min_distance = float('inf')
    max_coordinates = ()
    min_coordinates = ()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                min_coordinates = (points[i], points[j])
            if distance > max_distance:
                max_distance = distance
                max_coordinates = (points[i], points[j])

    return max_coordinates, min_coordinates


def main():
    points = []
    while True:
        os.system('cls')
        print("1)Ввод")
        print("2)Выполнение")
        print("3)Вывод")
        print("4)Выход")
        choice = input("Введите пункт меню:")

        if choice == "1":
            print("1)Вручную")
            print("2)Рандомно")
            choice1 = input("Введите пункт меню:")
            if choice1 == "1":
                while True:
                    try:
                        n = int(input("Количество точек:"))
                        break
                    except ValueError:
                        print("неверные значения")

                for i in range(n):
                    print("Координаты точки", i + 1)
                    while True:
                        try:
                            x = float(input("Введите x:"))
                            y = float(input("Введите y:"))
                            break
                        except ValueError:
                            print("неверные значения")

                    points.append((x, y))

                print(points)
            elif choice1 == "2":
                while True:
                    try:
                        n = int(input("Количество точек:"))
                        break
                    except ValueError:
                        print("неверные значения")

                    points = []
                for i in range(n):
                    x = random.randint(0, 100)
                    y = random.randint(0, 100)
                    points.append((x, y))
                print(points)
            else:
                print("Нет такого пункта")
            os.system('pause')

        elif choice == "2":
            max_coordinates, min_coordinates = find(points)
            print("Программа выполнилась")
            os.system("pause")
        elif choice == "3":
            print("Минимальная длинна:", min_coordinates)
            print("Максимальная длинна:", max_coordinates)
            os.system('pause')
        elif choice == "4":
            break
        else:
            print("Нет такого пункта")
            os.system('pause')


if __name__ == '__main__':
    main()
