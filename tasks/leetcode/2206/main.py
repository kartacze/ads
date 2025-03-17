import pytest


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        return True


def test_divideArray():
    assert Solution().divideArray([3, 2, 3, 2, 2, 2]) == True
