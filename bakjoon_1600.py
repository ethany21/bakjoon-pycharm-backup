from collections import deque
import sys

input = sys.stdin.readline

K = int(input())
M, N = map(int, input().split())

normal_x = [0, 0, 1, -1]
normal_y = [1, -1, 0, 0]

horse_x = [1, 2, 2, 1, -1, -2, -2, -1]
horse_y = [2, 1, -1, -2, -2, -1, 1, 2]

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs():
    queue = deque()
    queue.append((0, 0, K, 0))
    visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = True

    while queue:

        i, j, k, cnt = queue.popleft()

        if i == N - 1 and j == M - 1:
            return cnt

        if k > 0:
            for m in range(8):
                nx = i + horse_x[m]
                ny = j + horse_y[m]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny][k - 1] is False:
                    visited[nx][ny][k - 1] = True
                    queue.append((nx, ny, k - 1, cnt + 1))

        for m in range(4):
            nx = i + normal_x[m]
            ny = j + normal_y[m]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny][k] is False:
                visited[nx][ny][k] = True
                queue.append((nx, ny, k, cnt + 1))

    return -1


print(bfs())
