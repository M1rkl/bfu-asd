from random import randint
rand = [randint(-10, 100) for n in range(20)]
def merge(rand):
    if len(rand) > 1:
        mid = len(rand)//2
        left = rand[:mid]
        right = rand[mid:]
        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                rand[k] = left[i]
                i+=1
            else:
                rand[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            rand[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            rand[k] = right[j]
            j+=1
            k+=1
print(rand)
merge(rand)
print(rand)