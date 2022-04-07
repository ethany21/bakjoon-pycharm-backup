
T = int(input())

for _ in range(T):

    N = int(input())
    graph = {i: [] for i in range(1, N + 1)}

    for _ in range(N):
        parent, child = map(int, input().split())
        graph[parent].append((child, "child"))
        graph[child].append((parent, "parent"))

    print(graph)

if __name__ == "__main__":
    pass
