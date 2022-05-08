import sys


def find(a: int):
    if a == nodes[a]:
        return a
    nodes[a] = find(nodes[a])

    return nodes[a]


def union(a: int, b: int):
    a = find(a)
    b = find(b)

    if a < b:
        nodes[b] = a
    else:
        nodes[a] = b


if __name__ == "__main__":

    input = sys.stdin.readline

    sys.setrecursionlimit(10 ** 9)
    n, m = map(int, input().split())

    nodes = [i for i in range(n)]

    answer = 0
    for i in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            answer = i + 1
            break
        else:
            union(a, b)
    print(answer)
