# python3

#
# def giveSummands(i, l, n):
#
#     l.append(i)
#     if sum(l) == n:
#         return l
#     elif sum(l) < n:
#         return giveSummands(i+1, l, n)
#     elif sum(l) > n:
#         l.pop()
#         if len(l) > 0:
#             l.pop()
#         return giveSummands(i, l, n)


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    k = n # marked the upper part
    m = 1 # marked the lower part

    if n == 2 or n == 1:
     summands.append(n)
    else:
     for i in range(1,k):
         if k <= 2*m:
             summands.append(k)
             break
         else:
             summands.append(m)
             k = k - m
             m = m + 1

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
