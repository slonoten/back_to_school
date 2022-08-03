""" 
Дан список координат точек. Нужно определить можно ли провести через них
вертикальную прямую, чтобы точки были расположены симметрично относительно этой 
прямой
"""
from typing import List, Tuple


def is_symmetrical(points: List[Tuple[int, int]]) -> bool:
    if not points:
        return True
    x_coords = [x for x, _ in points]
    # Находим ось симметрии
    x_symmetry = (max(x_coords) + min(x_coords)) / 2
    # Строим set точек лежащих левее оси симметрии
    left_points = {point for point in points if point[0] < x_symmetry}
    # Симметрично, если для каждой точки справа от оси есть точка слева
    # Точки на оси в расчет не принимаем
    return all((2 * x_symmetry - x, y) in left_points for x, y in points if x > x_symmetry)


assert is_symmetrical([]), "Пустота - симметрична"

assert is_symmetrical([(1, 1)]), "Одна точка - всегда лежит на оси симметрии"

assert is_symmetrical([(1, 1), (2, 1)]), "Две точки на прямой параллельной оси X"

assert is_symmetrical(
    [(1, 2), (3, 2), (0, 5), (4, 5)]
), "4 точки с осью x=2"

assert is_symmetrical(
    [(1, 2), (3, 2), (0, 5), (4, 5), (2, 9), (2, 7)]
), "Точки на оси"

assert not is_symmetrical(
    [(1, 2), (3, 2), (0, 5), (4, 6)]
), "4 точки без симметрии"