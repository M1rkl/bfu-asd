from random import randint
rand = [randint(-10, 100) for n in range(20)]
def fast(rand, start, end):
    if end - start > 1:
        p = part(rand, start, end)
        fast(rand, start, p)
        fast(rand, p + 1, end)
def part(rand, start, end):
    pivot = rand[start]
    i = start + 1
    j = end - 1
    while True:
        while (i <= j and rand[i] <= pivot):
            i = i + 1
        while (i <= j and rand[j] >= pivot):
            j = j - 1

        if i <= j:
            rand[i], rand[j] = rand[j], rand[i]
        else:
            rand[start], rand[j] = rand[j], rand[start]
            return j

print(rand)
fast(rand, 0,len(rand))
print(rand)