# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    l = [0, 1]
    for i in range(m*m):
        l.append((l[-1]+l[-2]) % m)
        if l[-2] == 0 and l[-1] == 1:
            break
    l.pop()
    l.pop()
    #print(l, len(l))

    n = n % len(l)
    return l[n]
if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
