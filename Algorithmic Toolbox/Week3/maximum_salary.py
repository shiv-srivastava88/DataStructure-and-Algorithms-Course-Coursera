# python3

from itertools import permutations
from functools import cmp_to_key

def myFun(x, y):

    if x+y < y+x:
        return -1
    elif y+x > x+y:
        return 1
    else:
        return 0


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = cmp_to_key(myFun), reverse = True)
    s = ""
    for i in numbers:
        s = s + i

    return int(s)



if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
