import pytest


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        real_occupied = [0] * n
        result = [0] * n
        meetings_index = 0
        real_time = 0
        meetings.sort()

        while meetings_index < len(meetings):
            relative_min = min(real_occupied)

            meeting = meetings[meetings_index]

            start = meeting[0]
            end = meeting[1]

            for i in range(0, len(real_occupied)):
                room_time = real_occupied[i]

                if start >= room_time:
                    real_occupied[i] = end
                    result[i] += 1
                    meetings_index += 1
                    break

                if relative_min == real_occupied[i]:
                    real_occupied[i] = relative_min + end - start
                    result[i] += 1
                    meetings_index += 1
                    break
            # print("cc ", real_occupied, result)

        print("result", result)
        # result = [x for x in result if x > 0]
        return result.index(max(result))


def test_mostBooked():
    assert Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]) == 0
    assert Solution().mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]) == 1
    assert Solution().mostBooked(10, [[0, 1]]) == 0
    assert (
        Solution().mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4], [8, 11], [9, 12]])
        == 0
    )
    assert (
        Solution().mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]) == 0
    )
