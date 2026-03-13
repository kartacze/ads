class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return (2 ** n.bit_length() - 1) - n
        # return int("".join(["0" if v == "1" else "1" for v in format(n, "b")]), 2)
