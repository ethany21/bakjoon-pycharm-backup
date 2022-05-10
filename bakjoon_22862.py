import sys

input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))

if __name__ == "__main__":

    left, right = 0, 0
    answer = 0
    erased = 0
    while right < len(S):
        if erased <= K:
            if S[right] % 2 == 1:
                erased += 1
                right += 1
            else:
                right += 1
        else:
            if S[left] % 2 == 1:
                left += 1
                erased -= 1
            else:
                left += 1
        answer = max(answer, right - left - erased)

    print(answer)
