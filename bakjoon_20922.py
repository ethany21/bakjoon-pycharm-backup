if __name__ == "__main__":
    n, k = map(int, input().split())

    nodes = list(map(int, input().split()))

    left, right = 0, 0

    check = dict()
    answer = 0

    while right < len(nodes):

        if nodes[right] not in check:
            check[nodes[right]] = 1
            right += 1
        else:
            if check[nodes[right]] < k:
                check[nodes[right]] += 1
                right += 1
            else:
                check[nodes[left]] -= 1
                left += 1
        answer = max(answer, right - left)
    print(answer)
