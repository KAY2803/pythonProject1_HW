# Описать с помощью ООП любую геометрическиую фигуру.
# Установку значений производить или при инициализации экземпляра (через конструктор)
# или через специальные методы (сеттеры). Предусмотреть возможность получения различных параметров фигуры
# (периметр, площадь, радиус, длина сектора окружности и т.д) через методы (геттеры).
# Все типы устанавливаемых значений должны проверяться.
# Для класса реализовать метод repr.
# Создать несколько экземпляров класса вашей фигуры и напечатать их repr.

class Triangle:
    def __init__(self, line1: int, line2: int, line3: int):
        self.__line1 = self.__check_line1(line1, line2, line3)
        self.__line2 = self.__check_line2(line1, line2, line3)
        self.__line3 = self.__check_line3(line1, line2, line3)

    @staticmethod
    def __check_line1(line1, line2, line3):
        if not isinstance(line1, int):
            raise TypeError
        if line1 <= 0:
            raise ValueError
        if line1 < line2 + line3:
            __line1 = line1
        else:
            raise ValueError('значение line2 должно быть меньше суммы значений line1 и line3')
        return line1

    @staticmethod
    def __check_line2(line1, line2, line3):
        if not isinstance(line2, int):
            raise TypeError
        if line2 <= 0:
            raise ValueError
        if line2 < line1 + line3:
            __line2 = line2
        else:
            raise ValueError('значение line2 должно быть меньше суммы значений line1 и line3')
        return line2

    @staticmethod
    def __check_line3(line1, line2, line3):
        if not isinstance(line3, int):
            raise TypeError
        if line3 <= 0:
            raise ValueError
        if line3 < line1 + line2:
            __line3 = line3
        else:
            raise ValueError('значение line3 должно быть меньше суммы значений line1 и line2')
        return line3

    def get_perimetr(self):
        return f'Периметр экземпляра: {self} = {self.__line1 + self.__line2 + self.__line3}'

    def get_square(self):
        pp = self.__line1 + self.__line2 + self.__line3 / 2
        return f'Площадь экземпляра: {self} = {(pp * (pp - self.__line1) * (pp - self.__line2) * (pp - self.__line3)) ** 0.5:.2f}'

    def __repr__(self):
        return f'треугольник со сторонами {self.__line1}, {self.__line2}, {self.__line3}'


triangle1 = Triangle(5, 8, 10)
triangle2 = Triangle(24, 18, 35)
triangle3 = Triangle(150, 160, 170)

print(triangle1, triangle2, triangle3, sep='\n')
print(triangle2.get_perimetr())
print(triangle3.get_square())