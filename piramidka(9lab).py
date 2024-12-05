from random import randint
rand = [randint(-10, 100) for n in range(20)]
def heapify(rand, index, heaps):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heaps and rand[left_index] > rand[largest]:
        largest = left_index

    if right_index < heaps and rand[right_index] > rand[largest]:
        largest = right_index

    if largest != index:
        rand[largest], rand[index] = rand[index], rand[largest]
        heapify(rand, largest, heaps)

def heap(rand):

    n = len(rand)
    for i in range(n // 2 - 1, -1, -1):
        heapify(rand, i, n)
    for i in range(n - 1, 0, -1):
        rand[0], rand[i] = rand[i], rand[0]
        heapify(rand, 0, i)
    return rand

print(rand)
heap(rand)
print(rand)