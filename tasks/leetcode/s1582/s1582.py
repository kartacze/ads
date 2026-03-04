class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        result = 0
        for row in mat:
            if sum(row) == 1:
                one_index = row.index(1)
                result += 1 if sum([l[one_index] for l in mat]) == 1 else 0

        return result
