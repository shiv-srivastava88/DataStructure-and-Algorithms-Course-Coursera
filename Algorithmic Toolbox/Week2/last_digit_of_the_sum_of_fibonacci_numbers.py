# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    l = [0, 1]
    for i in range(59):
        l.append((l[-1] + l[-2]) % 10)
    n = n % 60
    s = sum(l[:n+1])
    return s% 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
