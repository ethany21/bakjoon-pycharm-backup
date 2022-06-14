import math

k: int = int(input())
nodes = list(map(int, input().split()))

if __name__ == "__main__":
    answer = []

    for i in range(k):
        idx = int(math.pow(2, i) - 1)
        box = []

        for j in range(idx, len(nodes), int(math.pow(2, (i + 1)))):
            box.append(nodes[j])
        answer.append(box)

    answer.sort(key=lambda x: len(x))

    for lst in answer:
        for node in range(len(lst)):
            print(lst[node], end=' ')
        print("")
