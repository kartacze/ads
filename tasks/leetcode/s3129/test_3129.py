from tasks.leetcode.s3129.s3129 import Solution


def test_numSpecial():
    s = Solution()
    assert s.numberOfStableArrays(3, 3, 2) == 14
    assert s.numberOfStableArrays(1, 1, 2) == 2
    assert s.numberOfStableArrays(1, 2, 1) == 1
    assert s.numberOfStableArrays(2, 2, 10) == 6
    assert s.numberOfStableArrays(14, 13, 59) == 14
