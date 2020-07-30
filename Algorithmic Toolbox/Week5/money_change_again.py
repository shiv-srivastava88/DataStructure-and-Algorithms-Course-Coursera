# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    l =[]
    for i in range(3):
        l1 = []
        for j in range(money+1):
            l1.append(0)
        l.append(l1)

    for i in range(1, money+1):
        l[0][i] = i

    coins = [1, 3, 4]
    for i in range(1, 3):
        coin = coins[i]
        for j in range(1, money+1):
            if j < coin:
                l[i][j] = l[i-1][j]
            else:
                l[i][j] = min(l[i-1][j], l[i][j-coin] + 1)
    return l[2][money]

if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
