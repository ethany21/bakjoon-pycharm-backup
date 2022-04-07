from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(N + 1)}
start = 1
end = 0
result = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if end < c:
        end = c
    graph[a].append((b, c))
    graph[b].append((a, c))

dot1, dot2 = map(int, sys.stdin.readline().split())


def bfs(begin: int, destination: int, max_cargo: int) -> bool:
    visited = [False for _ in range(N + 1)]

    queue = deque([begin])

    while queue:
        node = queue.popleft()
        visited[node] = True

        count = 0

        for tpl in graph[node]:
            next_node = tpl[0]
            weight_limit = tpl[1]
            if weight_limit > max_cargo and next_node != destination and not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                count += 1
            elif weight_limit > max_cargo and next_node == destination and not visited[next_node]:
                return True

        if count == 0:
            return False


while start <= end:

    mid = (start + end) // 2

    if bfs(begin=dot1, destination=dot2, max_cargo=mid):
        start = mid + 1
    else:
        end = mid - 1

if __name__ == '__main__':
    print(end)
