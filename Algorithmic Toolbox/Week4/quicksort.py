# python3

from random import randint


def partition3(array, left, right):
    lt = left
    rt = right
    i = left
    pivot = array[left]

    while i <= rt:
        if array[i] < pivot:
            array[lt], array[i] = array[i], array[lt]
            lt+=1
            i+=1
        elif array[i] > pivot:
            array[i], array[rt] = array[rt], array[i]
            rt-=1
        else:
            i+=1
    return lt, rt


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    lt, rt = partition3(array, left, right)
    randomized_quick_sort(array, left, lt-1)
    randomized_quick_sort(array, rt+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
