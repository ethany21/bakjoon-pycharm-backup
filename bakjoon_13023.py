from typing import List

depth = 0


def dfs(v, depth: int):
    global ans
    visited[v] = True

    if depth >= 4:
        ans = True
        return
    if ans:
        return

    for node in graph[v]:
        if not visited[node]:
            dfs(node, depth + 1)
            visited[node] = True


if __name__ == '__main__':
    N, M = map(int, input().split())

    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(N)]
    ans = False
    for i in range(N):
        dfs(i, 0)
        visited[i] = False
        if ans:
            break

    print(1 if ans else 0)
