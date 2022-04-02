N = int(input())
lst = list(map(int, input().split()))

result = (-1, -1)
compare = 1000000000 * 2

lst = sorted(lst, key=lambda x: abs(x), reverse=True)

for i in range(len(lst) - 1):

    if abs(compare) >= abs(lst[i] + lst[i + 1]):
        compare = lst[i] + lst[i + 1]
        result = (lst[i], lst[i + 1])

if __name__ == "__main__":
    result = sorted(result)
    print(result[0], result[1])
