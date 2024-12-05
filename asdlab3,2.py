import math
from itertools import product


def generate(x):
    results = set()  # Множество уникальных значений

    max_k = int((x // 3 + 1) ** 0.5) - 1
    max_l = int((x // 5 + 1) ** 0.5) - 1
    max_m = int((x // 7 + 1) ** 0.5) - 1

    powers = product(range(max_k + 1), range(max_l + 1), range(max_m + 1))

    for k, l, m in powers:
        num = 3 ** k * 5 ** l * 7 ** m
        if num <= x:
            results.add(num)

    return sorted(results)


x = int(input("Введите число x: "))
nujniyx = generate(x)
print(nujniyx)
