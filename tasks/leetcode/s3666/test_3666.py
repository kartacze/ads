from tasks.leetcode.s3666.s3666 import Solution

def test_sumRootToLeaf():
    s = Solution()
    assert s.minOperations("101", 2) == -1
    assert s.minOperations("110000", 2) == 2
    assert s.minOperations("110", 1) == 3
    assert s.minOperations("0101", 3) == 2
