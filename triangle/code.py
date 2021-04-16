import math


def triangle_perimeter(a, b, c):
    t_perimeter_value = a + b + c
    return t_perimeter_value


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    t_area_value = math.sqrt(p(p - a)(p - b)(p - c))
    return t_area_value


default_a = 7
default_b = 2
default_c = 8
