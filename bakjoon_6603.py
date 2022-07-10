from typing import List


def recurse(start, end: int, input_lst: List, box: List):
    if len(box) == 6:
        for b in box:
            print(b, end=' ')
        print()
        return

    for i in range(start, end):
        box.append(input_lst[i])
        recurse(i + 1, end, input_lst, box)
        box.pop()


if __name__ == "__main__":

    num_lst = []

    a = list(map(int, input().split()))
    while a[0] != 0:
        num_lst.append(a)
        a = list(map(int, input().split()))

    for lst in num_lst:
        recurse(0, lst[0], lst[1:], [])
        print()
