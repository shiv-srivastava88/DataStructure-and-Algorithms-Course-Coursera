# python3


def edit_distance(first_string, second_string):


    l =[]
    for i in range(len(second_string)+1):
        l1 = []
        for j in range(len(first_string)+1):
            l1.append(0)
        l.append(l1)

    for i in range(len(first_string)+1):
        l[0][i] = i

    for i in range(len(second_string)+1):
        l[i][0] = i

    for i in range(1, len(second_string)+1):
        for j in range(1, len(first_string)+1):

            if first_string[j-1] == second_string[i-1]:
                l[i][j] = l[i-1][j-1]
            else:
                l[i][j] = min(l[i-1][j], l[i-1][j-1], l[i][j-1])+1

    return l[len(second_string)][len(first_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
