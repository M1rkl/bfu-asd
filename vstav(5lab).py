from random import randint
def inser(rand):
    for i in range(1, len(rand)):
        temp = rand[i]
        j = i - 1
        while (j >= 0 and temp < rand[j]):
            rand[j + 1] = rand[j]
            j = j - 1
        rand[j + 1] = temp

rand = [randint(-10, 100) for n in range(20)]
print(rand)
inser(rand)
print(rand)