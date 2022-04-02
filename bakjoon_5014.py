from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False for _ in range(F + 1)]
count = [0 for _ in range(F + 1)]


def bfs():
    queue = deque()
    queue.append(S)

    visited[S] = True

    while queue:
        current = queue.popleft()
        if current == G:
            return count[G]

        for i in (current - D, current + U):
            if 0 < i <= F and visited[i] is not True:
                queue.append(i)
                visited[i] = True
                count[i] = count[current] + 1

    if count[G] == 0:
        return "use the stairs"


print(bfs())
