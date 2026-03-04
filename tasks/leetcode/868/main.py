class Solution:
    def binaryGap(self, n: int) -> int:
        bits = format(n, "b")
        dist = 0
        result = 0

        for val in bits[1:]:
            if val == "0":
                dist += 1
            else:
                result = max(result, dist + 1)
                dist = 0

        return result


def test_binaryGap():
    sol = Solution()
    assert sol.binaryGap(22) == 2
    assert sol.binaryGap(8) == 0
    assert sol.binaryGap(5) == 2
