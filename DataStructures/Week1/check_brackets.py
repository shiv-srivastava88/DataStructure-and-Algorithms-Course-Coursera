# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    firstOpened = 0
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            if opening_brackets_stack == []:
                firstOpened = i+1
            opening_brackets_stack.append(next)

        if next in ")]}":
            if opening_brackets_stack != [] and are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop()
            else:
                return i+1
    if (opening_brackets_stack != []):
        return firstOpened
    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
