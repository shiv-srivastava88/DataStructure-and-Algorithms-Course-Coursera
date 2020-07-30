# python3



def lcs2(first_sequence, second_sequence):

    l = []
    for i in range(len(first_sequence)+ 1):
        l1 = []
        for j in range(len(second_sequence) + 1 ):
            l1.append(0)
        l.append(l1)


    for i in range(1, len(first_sequence)+1):
        for j in range(1, len(second_sequence)+1):
            if second_sequence[j-1] == first_sequence[i-1]:
                l[i][j] = l[i-1][j-1]+1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1], l[i-1][j-1])

    return l[len(first_sequence)][len(second_sequence)]

n1 = int(input())
first = list(map(int, input().split()))
n2 = int(input())
second = list(map(int, input().split()))

print(lcs2(first, second))
