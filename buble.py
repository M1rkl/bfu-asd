from random import randint
def buble(num):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                # Меняем элементы
                num[i], num[i + 1] = num[i + 1], num[i]
                # Устанавливаем True для итерации
                swapped = True

# Проверяем работает ли
rnums = [randint(-10, 100) for n in range(20)]
print(rnums)
buble(rnums)
print(rnums)