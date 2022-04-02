N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
candidate = 0

while start <= end:
    mid = (start + end) // 2

    take = 0

    for tree in trees:
        if tree > mid:
            take += (tree - mid)

    if take >= M:
        candidate = mid
        start = mid + 1
    else:
        end = mid - 1

if __name__ == '__main__':
    print(candidate)
