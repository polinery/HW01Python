''' 2. Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''

x = int(input('X = '))
y = int(input('Y = '))
z = int(input('Z = '))
print(not (x or y or z) == (not x and not y and not z))
