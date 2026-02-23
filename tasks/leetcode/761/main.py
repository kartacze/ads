import functools
import itertools
from typing import List


class Solution:
    def findLowestCommonLevel(self, s: List[int]):
        # print("FIND")
        # print(s)
        ls = [(a, len(list(b))) for a, b in itertools.groupby(sorted(s))]
        # print(ls)
        first_common = next((x for (x, y) in ls if y >= 3), None)
        # print("FIRST")
        # print(first_common)
        if first_common != None:
            brk = [i for (i, v) in enumerate(s) if v == first_common]
            # print(brk)
            result = [s[0 : brk[0] + 1]]
            to_append = []
            for i in range(len(brk) - 1):
                to_append.append(
                    self.findLowestCommonLevel(s[brk[i] + 1 : brk[i + 1] + 1])
                )

            to_append.sort()
            to_append.reverse()
            result.extend(to_append)
            result.append(s[brk[-1] + 1 :])

            # print("RESULT")
            # print(result)

            return [x for l in result for x in l]
        else:
            return s

    def toString(self, s: List[int]):
        last = 0
        resp = []
        for val in s[1:]:
            if val > last:
                resp.append("1")
            else:
                resp.append("0")
            last = val
        return resp

    def makeLargestSpecial(self, s: str) -> str:
        # to mountain

        vals = map(int, list(s))

        acc = list(
            itertools.accumulate(
                vals, lambda a, b: a + (1 if b == 1 else -1), initial=0
            )
        )
        m = self.findLowestCommonLevel(acc)
        st = self.toString(m)
        return "".join(st)


def test_makeLargestSpecial():
    # assert Solution().makeLargestSpecial("11011000") == "11100100"
    assert Solution().makeLargestSpecial("1010101100") == "1100101010"
