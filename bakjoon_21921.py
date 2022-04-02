import sys

input = sys.stdin.readline

N, X = map(int, input().split())
visitor = list(map(int, input().split()))

max_sum = 0
max_count = 1

for i in range(len(visitor) - X + 1):

    if max_sum < sum(visitor[i:i + X]):
        max_sum = sum(visitor[i:i + X])
        max_count = 1

    elif max_sum == sum(visitor[i:i + X]):
        max_count += 1

if __name__ == "__main__":
    if max_sum == 0:
        print("SAD")
    print(max_sum)
    print(max_count)
