from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        

        max_c = 0
        l = len(nums)

        even_numbers = set[int]([])
        odd_numbers = set[int]([])
        diff = []
        i_edges = [0]
        i = 0

        # while s_i < len(nums):
        while i < l:
            val = nums[i]
            if val % 2 == 0:
                even_numbers.add(val)
            else:
                odd_numbers.add(val)
            diff.append(abs(len(even_numbers) - len(odd_numbers)))
            if i > 1:
                if diff[i - 2] >= diff[i - 1] and diff[i - 1] < diff[i]:

                    even_numbers.clear()
                    odd_numbers.clear()
                    i_edges.append(i - 1)
                    diff[i - 1] = 0
            i += 1

        i_edges.append(l - 1)

        print(i_edges)

        shift = 0
        # while len(i_edges) > 1:
        for s_edge in i_edges:
            for shift in range(0, 2):
                # s_edge = i_edges[0] if shift == 0 else i_edges[len(i_edges) - 1]
                e_edge = 0 if shift == 1 else len(nums) - 1

                print("LOOP")
                print(s_edge, e_edge)
                if max_c > (abs(s_edge - e_edge) + 3):
                    print("BREAK", max_c, s_edge, e_edge)
                    break

                even_numbers.clear()
                odd_numbers.clear()

                for i in range(
                    s_edge,
                    e_edge if shift == 0 else e_edge - 1,
                    1 if shift == 0 else -1,
                ):
                    val = nums[i]
                    if val % 2 == 0:
                        even_numbers.add(val)
                    else:
                        odd_numbers.add(val)

                    print("I", i, "VAL", val, len(even_numbers), len(odd_numbers))

                    if len(even_numbers) == len(odd_numbers):
                        c = abs(s_edge - i) + 1
                        print("CALC C", c, s_edge, i)
                        if c > max_c:
                            max_c = c

        print(i_edges)
        print(max_c)

        return max_c


# 100 101 102 101 100 99 98
# znajdz potencjalne krawedzie, pomte po staremu

# jezeli poprzedni byl mniejszy lub taki sam a nastepny jest wiekszy to to jest lokalna krawedz
# jezeli doszlismy do 0 to znaczy ze cala dlugosc jest blokiem


def test_longestBalanced():
    assert (
        Solution().longestBalanced(
            [49, 31, 16, 45, 61, 4, 43, 11, 61, 36, 49, 7, 42, 47, 26, 47, 42, 43]
        )
        == 8
    )
    assert Solution().longestBalanced([32, 42, 29, 6, 12]) == 2
    assert Solution().longestBalanced([30, 27, 25]) == 2
    assert Solution().longestBalanced([3, 2, 2, 5, 4]) == 5
    assert Solution().longestBalanced([1, 3, 5, 7, 9, 2]) == 2
    assert Solution().longestBalanced([1, 2, 3, 2]) == 3
    assert Solution().longestBalanced([2, 5, 4, 3]) == 4
