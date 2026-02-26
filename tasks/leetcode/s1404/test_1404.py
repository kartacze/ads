from tasks.leetcode.s1404.s1404 import Solution


def test_sumRootToLeaf():
    s = Solution()
    assert s.numSteps("1101") == 6
    assert s.numSteps("1001") == 7
