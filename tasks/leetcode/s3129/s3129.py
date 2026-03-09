import math


class Solution:
    def __init__(self):
        self.mem = {}

    def getNewtonian(self, r: int, n: int) -> int:
        return int(
            math.prod(range(1, n + 1))
            / (math.prod(range(1, n - r + 1)) * math.prod(range(1, r + 1)))
        )

    def numberOfStableArraysAux(
        self, last: str, total: int, zero: int, one: int, limit: int
    ) -> int:
        key = 

        if (zero + one) < limit:
            resp = self.getNewtonian(zero + one, one) % (10**9 + 7)
            print("RESP", resp)
            return resp

        if key in self.mem:
            return self.mem[key]

        if zero < 0 or one < 0:
            return 0

        if (len(arr) == (limit + 1)) and (
            ("0" in arr and (not "1" in arr)) or ("1" in arr and (not "0" in arr))
        ):
            return 0

        if zero == 0 and one == 0:
            return 1

        result = self.numberOfStableArraysAux(
            (arr + "0")[-(limit + 1) :], zero - 1, one, limit
        ) + self.numberOfStableArraysAux(
            (arr + "1")[-(limit + 1) :], zero, one - 1, limit
        )

        self.mem[key] = result

        return result

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        return self.numberOfStableArraysAux(
            "0", zero - 1, one, limit
        ) + self.numberOfStableArraysAux("1", zero, one - 1, limit)
