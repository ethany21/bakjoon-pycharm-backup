from collections import deque

A, B = map(int, input().split())


def bfs():
    visited = [A]
    queue = deque()
    queue.append([A, 1])

    while queue:
        candidate, count = queue.popleft()
        count += 1

        if candidate == B:
            return count
        elif candidate < B:
            if candidate not in visited:
                queue.append([candidate * 2, count])
                queue.append([candidate * 10 + 1, count])
    return -1


if __name__ == '__main__':
    print(bfs())
