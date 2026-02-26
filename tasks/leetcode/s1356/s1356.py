class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort()
        mem: list[list[int]] = [[] for _ in range(14)]

        for v in arr:
            bits = v.bit_count()
            mem[bits].append(v)

        return [i for x in mem for i in x]

        return []
