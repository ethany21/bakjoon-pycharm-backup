from collections import deque
import sys

input = sys.stdin.readline
case = int(input())

if __name__ == "__main__":

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for _ in range(case):
        M, N, lettuce = map(int, input().split())

        graph = [[0] * M for _ in range(N)]
        lst = []
        for _ in range(lettuce):
            a, b = map(int, input().split())
            graph[b][a] = 1
            lst.append((b, a))

        queue = deque()
        count = 0

        for tup in lst:
            i, j = tup
            if graph[i][j] == 1:
                queue.append([i, j])
                graph[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if graph[nx][ny] == 1:
                                graph[nx][ny] = 0
                                queue.append([nx, ny])
                count += 1
        print(count)
