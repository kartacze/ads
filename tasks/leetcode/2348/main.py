class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        total = 0
        nums.append(1)
        resp = 0

        for i in range(0, len(nums)):
            val = nums[i]
            if val == 0:
                total += 1
                resp += total
            else:
                total = 0

        return resp


def test_zeroFilledSubarray():
    assert Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    assert Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9
