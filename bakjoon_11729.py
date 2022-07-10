def recurse(n: int, one: int, two: int, three: int):
    if n == 1:
        print(one, three)
        return

    recurse(n - 1, one, three, two)
    print(one, three)
    recurse(n - 1, two, one, three)


def recurse2(n: int, one: int, two, three: int):
    if n > 1:
        recurse2(n - 1, one, three, two)

    print(one, three)

    if n > 1:
        recurse2(n - 1, two, one, three)


if __name__ == "__main__":
    num = int(input())

    print(pow(2, num) - 1)

    recurse2(num, 1, 2, 3)
