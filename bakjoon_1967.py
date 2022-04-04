import cProfile
from collections import deque
from itertools import count
from types import TracebackType
from typing import Dict
import operator

N = int(input())

graph = {i: [] for i in range(1, N+1)}

for _ in range(N - 1):
    a, b, distance = map(int, input().split())
    graph[a].append((b, distance))
    graph[b].append((a, distance))

def find_most_far(first: int, graph: Dict):

    queue = deque([first])
    visited = [False for _ in range(N+1)]

    count_distance = {first:0}

    while queue:

        node = queue.popleft()
        visited[node] = True

        for tup in graph[node]:
            next, value = tup[0], tup[1]
            if not visited[next]:
                count_distance[next] = count_distance[node] + value
                visited[next] = True
                queue.append(next)
    
    key= max(count_distance, key=count_distance.get)
    value = count_distance[key]

    return key, value

if __name__ == '__main__':

    first, first_dist = find_most_far(first=1, graph=graph)
    second, second_dist = find_most_far(first=first, graph=graph)
    print(second_dist)
