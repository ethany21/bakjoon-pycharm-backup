N = int(input())

requests = list(map(int, input().split()))
total_budget = int(input())

if __name__ == "__main__":

    if sum(requests) < total_budget:
        print(max(requests))
    else:
        start = 0
        end = max(requests)

        while start <= end:
            mid = (start + end) // 2
            compare = 0
            for i in range(len(requests)):
                if mid < requests[i]:
                    compare += mid
                else:
                    compare += requests[i]
            if compare <= total_budget:
                start = mid + 1
            else:
                end = mid - 1
        print(end)
