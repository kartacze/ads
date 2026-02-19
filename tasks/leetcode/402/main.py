from typing import List


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s: List[str] = ["0"]
        for number in num:
            while k and s and number < s[-1]:
                k -= 1
                s.pop()
            s.append(number)

        s = s[: len(s) - k]

        return "".join(s).lstrip("0") or "0"


def test_removeKdigits():
    assert Solution().removeKdigits("1432219", 3) == "1219"
    assert Solution().removeKdigits("10200", 1) == "200"
    assert Solution().removeKdigits("10", 3) == "0"
    assert Solution().removeKdigits("112", 1) == "11"
    assert Solution().removeKdigits("12345", 2) == "123"
    assert Solution().removeKdigits("1107", 1) == "107"
    assert Solution().removeKdigits("33526221184202197273", 19) == "0"
