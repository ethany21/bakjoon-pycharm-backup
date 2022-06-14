level = int(input())
tree = list(map(int, input().split()))


def divide_conquer(start, end, height):
    if start == end:
        answer[height].append(tree[start])
        return

    center = (start + end) // 2
    answer[height].append(tree[center])
    divide_conquer(start, center - 1, height + 1)
    divide_conquer(center + 1, end, height + 1)


if __name__ == "__main__":
    length = len(tree)
    answer = [[] for _ in range(level)]
    divide_conquer(0, length - 1, 0)
