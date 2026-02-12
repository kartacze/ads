from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        s: Set = {}


        s_i = 0
        max_c = 0

        even_numbers = set[int]([])
        odd_numbers = set[int]([])
        while s_i < len(nums):
            c = 1
            i = s_i
            even_numbers.clear()
            odd_numbers.clear()
            while i < len(nums):
                val = nums[i]
                if val % 2 == 0:
                    even_numbers.add(val)
                else:
                    odd_numbers.add(val)

                if len(even_numbers) == len(odd_numbers):
                    c = i - s_i + 1
                    if c > max_c:
                        max_c = c

                i += 1

            s_i += 1

        return max_c


def test_longestBalanced():
    assert Solution().longestBalanced([2,5,4,3]) == 4
    assert Solution().longestBalanced([1, 2, 3, 2]) == 3
