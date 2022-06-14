# N, M = map(int, input().split())
from collections import OrderedDict
from itertools import product

if __name__ == "__main__":
    for i in product([1, 3, 5, 7, 9]):
        print(i)
