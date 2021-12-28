# Описать с помощью ООП любую геометрическиую фигуру.
# Установку значений производить или при инициализации экземпляра (через конструктор)
# или через специальные методы (сеттеры). Предусмотреть возможность получения различных параметров фигуры
# (периметр, площадь, радиус, длина сектора окружности и т.д) через методы (геттеры).
# Все типы устанавливаемых значений должны проверяться.
# Для класса реализовать метод repr.
# Создать несколько экземпляров класса вашей фигуры и напечатать их repr.

class Triangle:
    def __init__(self, lines: [int, int, int]):
        self.__lines = self.__check_lines(lines)

    @staticmethod
    def __check_lines(lines):
        for line in lines:
            if not isinstance(line, int):
                raise TypeError
            if line <= 0:
                raise ValueError
        index = 0
        for _ in range(len(lines)):
            if lines[index] < lines[index + 1] + lines[index + 2]:
                line1 = lines[index]
            else:
                raise ValueError('значение line1 должно быть меньше суммы значений line1 и line3')
            if lines[index + 1] < lines[index] + lines[index + 2]:
                line2 = lines[index + 1]
            else:
                raise ValueError('значение line2 должно быть меньше суммы значений line1 и line3')
            if lines[index + 2] < lines[index + 1] + lines[index]:
                line3 = lines[index + 2]
            else:
                raise ValueError('значение line3 должно быть меньше суммы значений line1 и line3')
        return lines

    def get_perimetr(self):
        return f'Периметр экземпляра: {self} = {sum(self.__lines)}'

    def get_square(self):
        pp = sum(self.__lines) / 2
        return f'Площадь экземпляра: {self} = {(pp * (pp - self.__lines[0]) * (pp - self.__lines[1]) * (pp - self.__lines[2])) ** 0.5:.2f}'

    def __repr__(self):
        return f'треугольник со сторонами {self.__lines}'


triangle1 = Triangle([5, 8, 10])
triangle2 = Triangle([24, 18, 35])
triangle3 = Triangle([150, 160, 170])

print(triangle1, triangle2, triangle3, sep='\n')
print(triangle2.get_perimetr())
print(triangle3.get_square())