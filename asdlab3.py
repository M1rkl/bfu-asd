def generate(x):
    results = set()  # Множество уникальных значений
    max_k = 0
    max_l = 0  
    max_m = 0

    # Максимальные показатели K, L, M, чтобы не превышать x
    while 3**max_k <= x:
        max_k += 1
    while 5**max_l <= x:
        max_l += 1
    while 7**max_m <= x:
        max_m += 1

    # Генерируем числа не используя ранние вложенные циклов
    for k in range(max_k):
        p3 = 3**k
        for l in range(max_l):
            p5 = 5**l
            for m in range(max_m):
                p7 = 7**m
                number = p3 * p5 * p7
                if number <= x:  # Не превышает ли это число x
                    results.add(number)

    return sorted(results)


x = int(input("Введите число x: "))
nujniyx = generate(x)
print(nujniyx)