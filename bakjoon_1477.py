N, M, L = map(int, input().split())

gate = list(map(int, input().split()))

gate.extend([0, L])
gate.sort()

start = 1
end = L - 1

result = 0

while start <= end:

    cnt = 0
    mid = (start + end) // 2

    for i in range(1, len(gate)):

        if gate[i] - gate[i - 1] > mid:
            cnt += (gate[i] - gate[i - 1] - 1) // mid

    if cnt > M:
        start = mid + 1

    else:
        end = mid - 1
        result = mid

if __name__ == "__main__":
    print(result)
