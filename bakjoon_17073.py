from collections import deque

N, W = map(int, input().split())
tree = {
    i: [] for i in range(1, 1 + N)
}
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False for _ in range(N)]
queue = deque([1])
leaf_count = 0

while queue:
    current_node = queue.popleft()
    visited[current_node - 1] = True

    left_count = 0

    for node in tree[current_node]:
        if not visited[node - 1]:
            queue.append(node)
            left_count += 1
    if left_count == 0:
        leaf_count += 1

if __name__ == "__main__":
    if leaf_count != 0:
        print(W / leaf_count)
