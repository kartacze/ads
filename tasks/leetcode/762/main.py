import functools


class Solution:
    mem = dict({1: 0, 2: 1, 3: 1, 4: 0})

    def isPrime(self, val: int):
        if val in self.mem:
            return self.mem[val]
        isPrime = 1
        for i in range(2, int(val / 2)):
            if val % i == 0:
                isPrime = 0
                break
        self.mem[val] = isPrime
        return isPrime

    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = [self.isPrime(v.bit_count()) for v in range(left, right + 1)]
        return functools.reduce(lambda a, b: a + b, primes, initial=0)


def test_countPrimeSetBits():
    sol = Solution()
    assert sol.countPrimeSetBits(842, 888) == 23
    assert sol.countPrimeSetBits(6, 10) == 4
    assert sol.countPrimeSetBits(10, 15) == 5
