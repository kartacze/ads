class Solution:
    def minOperations(self, s: str, k: int) -> int:
        def countSteps(ones_num: int, zeros_num: int, k: int, step: int) -> int:
            if zeros_num == 0:
                return step
            if zeros_num % k == 0:
                full_steps = zeros_num // k
                return countSteps(
                    ones_num + (k * full_steps),
                    zeros_num - (k * full_steps),
                    k,
                    step + full_steps,
                )

            # here we are making space for a flip
            needed_zeros = k - (zeros_num % k)

            ones_change = 
            return countSteps(ones_num + )



            print(needed_zeros)
            return 0

        c_zero = len([i for i in s if i == "0"])
        c_one = len([z for z in s if z == "1"])
        if k > c_zero + c_one:
            return -1

        if k % 2 == 0 and c_zero % 2 != 0:
            return -1

        return countSteps(c_one, c_zero, k, 0)
