from random import randint
def shelly(rand):
    n = len(rand)
    a = n//2
    while a > 0:
        for i in range(a, n):
            temp = rand[i]
            j = i
            while j >= a and rand[j-a] > temp:
                rand[j] = rand[j-a]
                j -= a
                rand[j] = temp
            a //= 2
rand = [randint(-10, 100) for n in range(20)]
print(rand)
shelly(rand)
print(rand)