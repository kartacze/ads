from re import sub
import pytest


class Solution:
    def sumMeetings(self, startTime: list[int], endTime: list[int]) -> int:
        sum = 0
        for start, end in zip(startTime, endTime):
            sum += end - start
        return sum

    def freeTimeTotal(
        self, eventTime: int, startTime: list[int], endTime: list[int]
    ) -> int:
        return eventTime - self.sumMeetings(startTime, endTime)

    def tempFreeTime(
        self, eventTime: int, startTime: list[int], endTime: list[int]
    ) -> int:
        lens = [startTime[0], eventTime - endTime[-1]]
        for i in range(1, len(startTime)):
            lens.append(startTime[i] - endTime[i - 1])
        print(lens)
        return max(lens)

    def maxFreeTime(
        self, eventTime: int, k: int, startTime: list[int], endTime: list[int]
    ) -> int:
        maxFreeTime = self.freeTimeTotal(eventTime, startTime, endTime)

        if maxFreeTime == 0:
            return 0

        sizes = []
        for x in range(0, len(startTime) - k + 1):
            s = startTime.copy()
            e = endTime.copy()
            for i in range(x, x + k):
                if s[i] == e[i - 1]:
                    continue
                if i == 0:
                    s[i] = 0
                else:
                    s[i] = e[i - 1]
                e[i] = s[i] + endTime[i] - startTime[i]
            sizes.append(self.tempFreeTime(eventTime, s, e))

        return max(sizes)


def test_maxFreeTime():
    assert Solution().maxFreeTime(5, 1, [1, 3], [2, 5]) == 2
    assert Solution().maxFreeTime(10, 1, [0, 2, 9], [1, 4, 10]) == 6
    assert Solution().maxFreeTime(5, 2, [0, 1, 2, 3, 4], [1, 2, 3, 4, 5]) == 0
    assert Solution().maxFreeTime(21, 1, [7, 10, 16], [10, 14, 18]) == 7
    assert Solution().maxFreeTime(77, 2, [2, 51], [35, 61]) == 34
    assert Solution().maxFreeTime(182, 3, [2, 7, 49, 94], [4, 35, 85, 126]) == 82


#
#
# def test_freeTimeTotal():
#     assert Solution().freeTimeTotal(6, [1, 3], [2, 5]) == 3
#


#
def test_tempFreeTime():
    assert Solution().tempFreeTime(10, [0, 2, 9], [1, 4, 10]) == 5
    assert Solution().tempFreeTime(10, [0], [2]) == 8
    assert Solution().tempFreeTime(10, [3], [10]) == 3
    assert Solution().tempFreeTime(10, [], []) == 10


# def test_getBestFill():
#     assert Solution().getBestFill(10, [0, 2, 9, 10], [1, 4, 10, 10], 1) == 5


# class main:
#     Solution().maxFreeTime(5, 1, [1, 3], [2, 5])
