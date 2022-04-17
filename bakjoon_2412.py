import sys

n, T = map(int, sys.stdin.readline().split())

coordinates = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    coordinates.append([a, b])

start = 1
end = 50000


def bfs() -> bool:
    return False
