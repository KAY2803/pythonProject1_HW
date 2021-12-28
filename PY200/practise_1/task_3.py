# Описать фигуру в пространстве и отрисовать её

import plotly.graph_objects as go

class Triangle:
    def __init__(self, coordinates: [int, int, int, int], color: tuple[int, int, int]):
        self.__coordinates = self.__check_coordinates(coordinates)
        self.__color = self.__check_color(color)


    @staticmethod
    def __check_coordinates(coordinates):
        for num in coordinates:
            if not isinstance(num, int):
                raise TypeError
            if len(str(num)) > 3:
                raise ValueError('Число должно иметь не менее трех цифр')
            return coordinates

    @staticmethod
    def __check_color(color: tuple[int, int, int]):
        for num in color:
            if not isinstance(num, int):
                raise TypeError
            if 0 > num:
                raise ValueError('Число должно быть от 0 до 255')
            if 255 < num:
                raise ValueError('Число должно быть от 0 до 255')
        return color

    def get_color(self):
        return f'rgb{self.__color}'

    def get_coordinates(self):
        x = []
        y = []
        z = []
        for num in map(str, self.__coordinates):
            if num == '0':
                x.append('0')
                y.append('0')
                z.append('0')
            else:
                x.append(str(num[0]))
                y.append(str(num[1]))
                z.append(str(num[2]))
        x = list(map(int, x))
        y = list(map(int, y))
        z = list(map(int, z))
        return x, y, z

    def __str__(self):
        return f'треугольник с координатами {self.__coordinates} цвета {self.__color}'

triangle1 = Triangle([111, 213, 321, 132], (253, 200, 100,))
triangle1.intensity = [3, 5, 10, 20, 28]


fig = go.Figure(data=[
    go.Mesh3d(
        x=triangle1.get_coordinates()[0],
        y=triangle1.get_coordinates()[1],
        z=triangle1.get_coordinates()[2],
        alphahull=0,
        intensity=triangle1.intensity,
        color=triangle1.get_color()
            )
])

fig.show()
