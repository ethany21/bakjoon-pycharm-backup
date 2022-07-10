def recurse(n: int):
    if n == 1 or n == 0:
        return n

    before_1 = recurse(n - 1)
    before_2 = recurse(n - 2)
    return before_2 + before_1


if __name__ == "__main__":

    print(recurse(6))
