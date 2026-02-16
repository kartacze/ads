from typing import List

# Top down approach


class Solution:
    def __init__(self):
        self.mem = {0: 0}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1

        if amount in self.mem:
            return self.mem[amount]

        if amount in coins:
            resp = 1
        else:
            cl = ((self.coinChange(coins, amount - c)) for c in reversed(coins))
            cl = list(cl)
            cl = [x for x in cl if x >= 0]
            if len(cl) == 0:
                resp = -1
            else:
                resp = min(cl) + 1

        self.mem[amount] = resp
        return resp


def test_coinChange():
    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 3) == -1
    assert Solution().coinChange([5], 11) == -1
    assert Solution().coinChange([1], 0) == 0
