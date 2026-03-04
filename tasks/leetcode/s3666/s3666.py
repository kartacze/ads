class Solution:
    def minOperations(self, s: str, k: int) -> int:
        c_zero = len([i for i in s if i == "0"])
        c_one = len([z for z in s if z == "1"])

        if k % 2 == 0:
            if (c_zero - c_one) % 2 == 0:
                return (c_zero - c_one) // k
            else:
                return -1

        return 5
