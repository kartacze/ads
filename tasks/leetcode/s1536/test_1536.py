from tasks.leetcode.s1536.s1536 import Solution


def test_sumRootToLeaf():
    s = Solution()
    assert s.minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]) == 3
