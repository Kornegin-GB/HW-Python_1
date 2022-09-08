""" Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. """

count = 0

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not (x or y or z) == (not x and not y and not z):
                print(f'{count + 1}) ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}')
                count += 1

if count == 2**3:
    print('Утверждение ИСТИНА')
else:
    print('Утверждение ЛОЖЬ')
