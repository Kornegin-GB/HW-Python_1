""" Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). """

number_quarter = int(input('Введите номер координатной четверти: '))

if number_quarter == 1:
    print('Диапазон координат X > 0 и Y > 0')
elif number_quarter == 2:
    print('Диапазон координат X < 0 и Y > 0')
elif number_quarter == 3:
    print('Диапазон координат X < 0 и Y < 0')
elif number_quarter == 4:
    print('Диапазон координат X > 0 и Y < 0')
elif number_quarter < 1 or number_quarter > 4:
    print('Нет такой четверти')
