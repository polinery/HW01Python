''' 4. Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y). '''

quarter = int(input('Введите номер четверти координатной плоскости '))
if quarter == 1:
    coordinates = 'x > 0, y > 0'
elif quarter == 2:
    coordinates = 'x < 0, y > 0'
elif quarter == 3:
    coordinates = 'x < 0, y < 0'
elif quarter == 4:
    coordinates = 'x > 0, y < 0'
print(f'Диапазон координат: ({coordinates})')
