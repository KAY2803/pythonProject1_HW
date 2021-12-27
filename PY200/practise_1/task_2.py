# Добавить установку параметров цвета фигуры (цвет окружности + ширина, цвет заливки фигуры)
# через шестнадцатеричное значение ('#FFFFFF') или через кортеж с RGB значениями (255, 123, 233).
# Предусмотреть валидацию цвета.
#
# Отрисовать фигуру с помощью библиотеки Plotly или Matplotlib.

import plotly

from typing import Optional
import plotly.graph_objs as go


class Triangle:
    def __init__(self, coordinates: [int, int, int], color_line: tuple[int, int, int]):
        self.__coordinates = self.__check_coordinates(coordinates)
        #self.__lines = self.__check_lines(lines)
        self.__lines = None
        self.init_lines()
        self.__color_line = self.__check_color_line(color_line)
        self.__width_line = 5
        self.__color_fill = 'rgb(255, 230, 110)'


    @staticmethod
    def __check_coordinates(coordinates):
        for num in coordinates:
            if not isinstance(num, int):
                raise TypeError
            if len(str(num)) > 2:
                raise ValueError('Число должно иметь не менее двух цифр')
            return coordinates

    # @staticmethod
    # def __check_lines(lines):
    #     for line in lines:
    #         if not isinstance(line, int):
    #             raise TypeError
    #         if line <= 0:
    #             raise ValueError
    #     index = 0
    #     for _ in range(len(lines)):
    #         if lines[index] < lines[index + 1] + lines[index + 2]:
    #             line1 = lines[index]
    #         else:
    #             raise ValueError('значение line1 должно быть меньше суммы значений line1 и line3')
    #         if lines[index + 1] < lines[index] + lines[index + 2]:
    #             line2 = lines[index + 1]
    #         else:
    #             raise ValueError('значение line2 должно быть меньше суммы значений line1 и line3')
    #         if lines[index + 2] < lines[index + 1] + lines[index]:
    #             line3 = lines[index + 2]
    #         else:
    #             raise ValueError('значение line3 должно быть меньше суммы значений line1 и line3')

    def init_lines(self):
        line1 = ((self.get_coordinates()[0][1] - self.get_coordinates()[0][0]) ** 2
                + (self.get_coordinates()[1][1] - self.get_coordinates()[1][0]) ** 2) ** 0.5
        line2 = (line1 ** 2 + (self.get_coordinates()[0][1] - self.get_coordinates()[0][0]) ** 2) ** 0.5
        line3 = (line1 ** 2 + line2 ** 2) ** 0.5
        self.__lines = line1, line2, line3

    @staticmethod
    def __check_color_line(color_line: tuple[int, int, int]):
        for num in color_line:
            if not isinstance(num, int):
                raise TypeError
            if 0 > num:
                raise ValueError('Число должно быть от 0 до 255')
            if 255 < num:
                raise ValueError('Число должно быть от 0 до 255')
        return color_line

    def get_color_line(self):
        return f'rgb{self.__color_line}'

    def get_width_line(self):
        return self.__width_line

    def get_color_fill(self):
        return self.__color_fill

    def get_coordinates(self):
        x = []
        y = []
        for num in map(str, self.__coordinates):
            if num == '0':
                x.append('0')
                y.append('0')
            else:
                x.append(str(num[0]))
                y.append(str(num[1]))
        x = list(map(int, x))
        x.append(x[0])
        y = list(map(int, y))
        y.append(y[0])
        return x, y

    def get_perimetr(self):
        return f'Периметр экземпляра: {self} = {self.__lines[0] + self.__lines[1] + self.__lines[2]:.2f}'

    def get_square(self):
        pp = self.__lines[0] + self.__lines[1] + self.__lines[2] / 2
        return f'Площадь экземпляра: {self} = {(pp * (pp - self.__lines[0]) * (pp - self.__lines[1]) * (pp - self.__lines[2])) ** 0.5:.2f}'

    def __repr__(self):
        return f'треугольник со сторонами {self.__lines[0]:.2f}, {self.__lines[1]:.2f}, {self.__lines[2]:.2f}' \
               f' линией цвета rgb{self.__color_line}'


triangle1 = Triangle([00, 50, 45], (255, 123, 233,))
print(triangle1)

fig = go.Figure(go.Scatter(
    x=triangle1.get_coordinates()[0],
    y=triangle1.get_coordinates()[1],
    line=dict(
        color=triangle1.get_color_line(),
        width=triangle1.get_width_line()
    ),
    fill="toself",
    fillcolor=triangle1.get_color_fill()))
fig.show()
