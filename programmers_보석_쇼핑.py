def solution(gems):
    compare = set(gems)
    candidate = []
    start, end = 0, 0

    while end <= len(gems):

        if set(gems[start:end]) != compare:
            end += 1
        else:
            candidate.append([start + 1, end])
            while start < end:
                if set(gems[start:end]) == compare:
                    candidate.append([start + 1, end])
                start += 1

    answer = min(candidate, key=lambda x: x[1] - x[0])
    return answer


if __name__ == '__main__':
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))
    print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
    print(solution(["AA", "AB", "AC", "AA", "AC"]))
    print(solution(["XYZ", "XYZ", "XYZ"]))