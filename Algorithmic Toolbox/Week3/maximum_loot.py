# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    l = []
    for i in range(len(weights)):
        l.append([weights[i], prices[i], prices[i] / weights[i]])

    l.sort(key = lambda l : l[2], reverse = True)

    current_weight = 0
    price=0
    for i in l:
        if current_weight + i[0] <= capacity:
            current_weight += i[0]
            price += i[1]
        else:
            price += (capacity-current_weight) * i[2]
            break
    return price


if __name__ == "__main__":
    items_capacity = list(map(int, input().split()))
    input_weights = []
    input_prices = []
    for i in range(items_capacity[0]):
        wp = list(map(int, input().split()))
        input_weights.append(wp[1])
        input_prices.append(wp[0])
    opt_value = maximum_loot_value(items_capacity[1], input_weights, input_prices)
    print("{:.10f}".format(opt_value))
    # wei = list(map(int, input().split()))
    # pri = list(map(int, input().split()))
    # cap = int(input())
    # print(maximum_loot_value(cap, wei, pri))
