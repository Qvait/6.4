import math


class Figure():
    a = False
    sides_count = 0

    def __init__(self, __sides=[1], __color=(22, 22, 22), filled=False):
        if all(isinstance(i, int) for i in __sides):
            self.__sides = __sides
        else:
            print("Стороны должны быть целыми числами.")

        if len(__color) == 3 and all(0 <= i <= 255 for i in __color):
            self.__color = __color
        else:
            print(f"Цвет не в формате r g b. Должно быть 3 числа от 0 до 255.")

        self.filled = filled

    def __is_valid_sides(self, *sides):
        if all(isinstance(side, int) for side in sides):
            return len(sides) == len(self.__sides)
        return False

    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if max(r, g, b) <= 255 and min(r, g, b) >= 0:
            print("Значения подходят для смены цвета")
            Figure.a = True
        else:
            print("Значения не подходят для смены цвета")
            Figure.a = False

    def set_color(self, r, g, b):
        self.__is_valid_color(r, g, b)
        if Figure.a:
            self.__color = [r, g, b]
            print(f"Цвет изменен на {self.__color}")

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.sides_count == len(new_sides):
            self.__sides = new_sides
            print("Стороны изменены")
        else:
            print("Количество сторон не верно")


class Circle(Figure):
    sides_count = 1

    def __init__(self, __sides=[1], __color=(22, 22, 22), filled=False):
        super().__init__(__sides, __color, filled)  # Вызов конструктора родителя
        if len(__sides) == 1:
            self.__sides = __sides
            self.__radius = self.__sides[0] / (2 * math.pi)
        else:
            print("Количество сторон не верно.")

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __sides=[1], __color=(22, 22, 22), filled=False):
        super().__init__(__sides, __color, filled)  # Вызов конструктора родителя
        if len(__sides) == 3:
            self.__sides = __sides
        else:
            if len(__sides) > 3:
                print("Слишком много сторон")
            else:
                while len(__sides) < 3:
                    __sides.append(__sides[0])
                self.__sides = __sides

    def get_square(self):
        b = sum(self.__sides) / 2  # Полупериметр
        return math.sqrt(b * (b - self.__sides[0]) * (b - self.__sides[1]) * (b - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, __sides=[1], __color=(22, 22, 22), filled=False):
        super().__init__(__sides, __color, filled)  # Вызов конструктора родителя
        if len(__sides) == 1:
            a = __sides[0]
            self.__sides = [a] * 12  # Заполнение 12 одинаковыми сторонами
        else:
            print("Куб неверен")

    def get_volume(self):
        return self.__sides[0] ** 3  # Объем куба


circle1 = Circle([10], (200, 200, 100))
cube1 = Cube([6], (222, 35, 130))

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())