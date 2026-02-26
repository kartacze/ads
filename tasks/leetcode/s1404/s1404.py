class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        v = int(s, 2)
        while v != 1:
            if v % 2 == 0:
                steps += 1
                v = v // 2
            else:
                steps += 2
                v = (v // 2) + 1

        return steps

