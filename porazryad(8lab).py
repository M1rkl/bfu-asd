from random import randint
rand = [randint(1, 100) for n in range(20)]
def counting_Sort(rand, p):
    s = len(rand)
    result = [0] * s
    c = [0] * 10

    for i in range(0, s):
        index = rand[i] // p
        c[index % 10] += 1

    for i in range(1, 10):
        c[i] += c[i - 1]

    i = s - 1
    while i >= 0:
        index = rand[i] // p
        result[c[index % 10] - 1] = rand[i]
        c[index % 10] -= 1
        i -= 1

    for i in range(0, s):
        rand[i] = result[i]

def porezryad(rand):
    maximum = max(rand)

    p = 1
    while maximum // p > 0:
        counting_Sort(rand, p)
        p *= 10

print(rand)
porezryad(rand)
print(rand)
