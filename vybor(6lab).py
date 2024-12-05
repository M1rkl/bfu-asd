from random import randint
def select(rand):
    for i in range(0, len(rand) - 1):
        smallest = i
        for j in range(i + 1, len(rand)):
            if rand[j] < rand[smallest]:
                smallest = j
        rand[i], rand[smallest] = rand[smallest], rand[i]

rand = [randint(-10, 100) for n in range(20)]
print(rand)
select(rand)
print(rand)