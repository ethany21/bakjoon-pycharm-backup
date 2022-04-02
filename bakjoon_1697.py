from collections import deque

N, K = map(int, input().split())

visited = [False for _ in range(100001)]
count = [0 for _ in range(100001)]
visited[N] = True
queue = deque()
queue.append(N)

while queue:
    current = queue.popleft()

    if current == K:
        print(count[current])
        break

    for i in (current - 1, current + 1, 2 * current):
        if 0 <= i <= 100000 and not visited[i]:
            count[i] = count[current] + 1
            visited[i] = True
            queue.append(i)
