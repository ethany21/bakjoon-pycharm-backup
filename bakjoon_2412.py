import sys
from collections import deque

n, T = map(int, sys.stdin.readline().split())

coordinates = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    coordinates.append([a, b, 0])

start = 1
end = 50000
result = 0


def bfs(count_limit: int) -> bool:
    visited = [False for _ in range(n)]

    queue = deque()

    queue.append([0, 0, 0])
    while queue:
        current = queue.popleft()

        if current[2] > count_limit:
            return False
        elif current[1] == T:
            return True
        for i in range(n):
            if not visited[i] and abs(coordinates[i][0] - current[0]) <= 2 and abs(coordinates[i][1] - current[1]) <= 2:
                coordinates[i][2] = current[2] + 1
                queue.append(coordinates[i])
                visited[i] = True

    return False


while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        end = mid - 1
    else:
        start = mid + 1
        result = start

if __name__ == '__main__':
    if start == 50001:
        print(-1)
    else:
        print(result)
