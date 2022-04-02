N, K = map(int, input().split())

start = 0
end = N
if N % 2 == 0:
    start = int(N // 2)

else:
    start = int((N - 1) / 2)

mid = int((start + end) // 2)

while start <= end:

    compare = (mid + 1) * (N - mid + 1)

    if compare == K:
        break

    elif compare < K:
        end = mid - 1

    else:
        start = mid + 1

    mid = int((start + end) // 2)

if __name__ == "__main__":

    if (mid + 1) * (N - mid + 1) == K:
        print("YES")
    else:
        print("NO")
