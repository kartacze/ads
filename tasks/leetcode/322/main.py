class Solution:
    def __init__(self):
        self.mem = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        print(self.mem)
        if amount in self.mem:
            return self.mem[amount]
        
        resp = 0
        if amount in coins:
            resp = 1
        else 3

        self.mem[amount] = resp
        return resp
