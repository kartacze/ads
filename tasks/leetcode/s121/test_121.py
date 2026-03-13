from tasks.leetcode.s121.s121 import Solution


def test_numSpecial():
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([100, 0, 1]) == 1
    assert s.maxProfit([100, 102, 0, 1]) == 2
