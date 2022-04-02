# from collections import deque
# from sys import stdin
#
# input = stdin.readline
#
# queue = deque()
# visited = dict()
#
# N, K = map(int, input().split())
#
# fond = list(map(int, input().split()))
#
# for water in fond:
#     queue.append(water)
#     visited[water] = 0
#
# while queue:
#
#     if K <= 0:
#         break
#
#     present = queue.popleft()
#
#     for candidate in [present - 1, present + 1]:
#         if candidate not in queue and K > 0:
#             visited[candidate] = visited[present] + 1
#             K -= 1
#             queue.append(candidate)
#
# result = 0
# for val in visited.values():
#     result += val
#
# print(result)

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())  # 샘터 수, k채 집
n_list = list(map(int, sys.stdin.readline().split()))  # 샘터 위치
visit = set()

dq = deque()
# 1. 샘터를 기준으로 시작하기 위해 큐에 넣어준다.
for i in n_list:
    dq.append((i, 1))  # 위치, 불행도
    visit.add(i)  # 방문 체크

# 2. -1, + 1 위치 방향으로 bfs 진행
result = 0  # 불행도의 합 최솟값
now_build = 0  # 현재까지 지어진 집 수
while dq:
    now, b = dq.popleft()  # 위치, 불행도
    for d in [1, -1]:
        nx = now + d  # 새로 지은 집 위치
        if nx not in visit:  # 방문 여부 체크
            visit.add(nx)  # 방문 체크
            result += b  # 결과에 불행도 증가
            now_build += 1  # 지어진 집 수 + 1
            dq.append((nx, b + 1))  # 집 위치, 집에 대한 불행도 + 1
            if now_build == k:
                dq = list()
                break
print(result)
