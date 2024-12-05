from random import randint

rand = [randint(-10, 100) for n in range(20)]
print(rand)

x = 1.247
distance = len(rand)
while (distance := int(distance // x)) >= 1:
    for i in range(len(rand)-distance):
        if rand[i] > rand[distance+i]:
            rand[i], rand[distance+i] = rand[distance+i], rand[i]
print(rand)
