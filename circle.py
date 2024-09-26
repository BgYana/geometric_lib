import math


def area(r: float) -> float:
    """
    Вычисляет площадь круга по заданному радиусу.

    :param r: Радиус круга
    :return: Площадь круга
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
    Вычисляет периметр (длину окружности) круга по заданному радиусу.

    :param r: Радиус круга
    :return: Периметр круга
    """
    return 2 * math.pi * r
