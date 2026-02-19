import itertools
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = [[len(list(v)), x] for x, v in itertools.groupby(sorted(nums))]
        r = sorted(s, key=lambda x: x[0], reverse=True)
        return [x[1] for x in r[:k]]


def test_removeKdigits():
    assert Solution().topKFrequent(nums=[1, 1, 1, 3, 1, 2, 2, 2, 3], k=2) == [1, 2]
    assert Solution().topKFrequent(nums=[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2) == [1, 2]
    assert Solution().topKFrequent(nums=[1], k=1) == [1]
