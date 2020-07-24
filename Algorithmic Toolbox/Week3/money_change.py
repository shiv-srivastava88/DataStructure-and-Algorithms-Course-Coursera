# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    tens = money // 10
    money = money % 10
    fives = money // 5
    money = money % 5
    return tens + fives + money


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
