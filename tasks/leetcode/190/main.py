class Solution:
    def reverseBits(self, n: int) -> int:
        bits = format(n, "b")
        for i in range(len(bits), 32):
            bits = "0" + bits
        rev = bits[::-1]
        return int(rev, 2)


def test_reverseBits():
    assert Solution().reverseBits(43261596) == 964176192
