""" Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
A (3,6); B (2,1) -> 5,09
A (7,-5); B (1,-1) -> 7,21 """

from math import sqrt

ax = int(input('Ax = '))
ay = int(input('Ay = '))

bx = int(input('Bx = '))
by = int(input('By = '))

distance_between_two_points = round(sqrt(((ax-bx) ** 2) + ((ay-by) ** 2)), 2)

print(distance_between_two_points)
