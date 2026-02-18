from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack: List[str] = [num[0]]
        removals = k
        for val in num[1:]:
            if removals > 0:
                last = stack.pop()
                if val == "0" and len(stack) == 0:
                    stack.append(last + "0")
                elif int(val) >= int(last):
                    stack.append(last)
                    stack.append(val)
                else:
                    stack.append(val)
                    removals -= 1

            else:
                stack.append(val)

        if removals != 0:
            stack = stack[0:-removals]

        if stack == []:
            return "0"

        return "".join(stack)


def test_removeKdigits():
    assert Solution().removeKdigits("1432219", 3) == "1219"
    assert Solution().removeKdigits("10200", 1) == "200"
    assert Solution().removeKdigits("10", 3) == "0"
    assert Solution().removeKdigits("112", 1) == "11"
    assert Solution().removeKdigits("12345", 2) == "123"
    assert Solution().removeKdigits("1107", 1) == "107"
    assert Solution().removeKdigits("33526221184202197273", 19) == "0"
