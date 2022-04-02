K, N = map(int, input().split())

lan = []
for _ in range(K):
    lan.append(int(input()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2

    compare = 0

    for num in lan:
        compare += num // mid

    if compare >= N:
        start = mid + 1

    else:
        end = mid - 1

if __name__ == '__main__':
    print(end)
