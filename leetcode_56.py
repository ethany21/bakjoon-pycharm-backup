# Definition for singly-linked list.

from typing import List, Optional


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])

        answer = [intervals[0]]
        del intervals[0]

        for i in range(len(intervals)):
            front = answer[-1]
            back = intervals[i]

            if front[1] >= back[1]:
                front = [front[0], front[1]]
                answer[-1] = front
            elif back[0] <= front[1] < back[1]:
                front = [front[0], back[1]]
                answer[-1] = front
            else:
                answer.append(intervals[i])

        return answer


if __name__ == "__main__":
    intervals2 = [[1, 4], [0, 2], [3, 5]]
    sol = Solution()

    print(sol.merge(intervals2))
