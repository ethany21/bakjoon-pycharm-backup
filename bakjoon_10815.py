import sys

input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))
answer = [0] * M

card.sort()

for idx in range(len(compare)):
    start = 0
    end = len(card) - 1
    while start <= end:

        mid = (start + end) // 2
        if card[mid] == compare[idx]:
            answer[idx] = 1
            del card[mid]
            break
        elif card[mid] < compare[idx]:
            start = mid + 1

        else:
            end = mid - 1

if __name__ == '__main__':
    for i in answer:
        print(i, end=" ")
