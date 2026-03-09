from tasks.leetcode.s1758.s1758 import Solution


def test_numSpecial():
    s = Solution()
    assert s.minOperations("0100") == 1
    assert s.minOperations("1111") == 2
    assert s.minOperations("01") == 0
