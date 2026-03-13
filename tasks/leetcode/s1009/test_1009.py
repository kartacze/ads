from tasks.leetcode.s1009.s1009 import Solution


def test_numSpecial():
    s = Solution()
    assert s.bitwiseComplement(5) == 2
    assert s.bitwiseComplement(7) == 0
    assert s.bitwiseComplement(10) == 5
