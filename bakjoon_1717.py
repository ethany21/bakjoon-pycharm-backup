import sys

input = sys.stdin.readline

N, M = map(int, input().split())

parent = []
for i in range(N + 1):
    parent.append(i)


def find(x):
    if x == parent[x]:
        return x

    a = find(parent[x])
    parent[x] = a

    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def check_same_parent(x, y):
    x = find(x)
    y = find(y)
    return x == y


if __name__ == "__main__":
    for _ in range(M):
        o, a, b = map(int, input().split())
        if o:
            print("YES" if check_same_parent(a, b) else "NO")

        else:
            union(a, b)
