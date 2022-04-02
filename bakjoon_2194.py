from collections import deque
from typing import List

N, M, A, B, K = map(int, input().split())

huddle = [list(map(int, input().split())) for _ in range(K)]
start = list(map(int, input().split()))
end = list(map(int, input().split()))

visited = [[False] * M for _ in range(N)]
count = [[0] * M for _ in range(N)]

for i in range(2):
    start[i] -= 1
    end[i] -= 1

graph = [[0] * M for _ in range(N)]
for i in range(K):
    graph[huddle[i][0] - 1][huddle[i][1] - 1] = 1


def movable(current: List) -> bool:

    for i in range(A):
        if graph[current[i]][current[1] + 1] == 1 or graph[current[i]][current[1] + 1] > M - 1:
            pass

    return True


queue = deque()

queue.append(start)
