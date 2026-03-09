class Solution:
    def minOperations(self, s: str) -> int:
        check_zero = "0"
        check_one = "1"

        result_zero = 0
        result_one = 0

        for num in s:
            if num != check_zero:
                result_zero += 1
            else:
                result_one += 1

            keep = check_zero
            check_zero = check_one
            check_one = keep

        return min(result_one, result_zero)
