class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        output = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):
                    if (
                        abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[i] - arr[k]) <= c
                    ):
                        output += 1

        return output


def test_case_1():
    assert Solution().countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3) == 4


def test_case_2():
    assert Solution().countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1) == 0
