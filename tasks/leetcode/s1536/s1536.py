from typing import Tuple


class Solution:
    def validRow(self, row: list[int], i: int) -> bool:
        return all(s == 0 for s in row[i + 1 :])

    def swap(
        self, grid: list[list[int]], j: int, i: int
    ) -> tuple[list[list[int]], int]:
        if i == j:
            return (grid, 0)
        grid = grid[0:i] + [grid[j]] + grid[i:j] + grid[j + 1 :]
        return (grid, j - i)

    def minSwaps(self, grid: list[list[int]]) -> int:
        moves = 0

        for i in range(len(grid) - 1):
            switch = None
            for j in range(i, len(grid)):
                if self.validRow(grid[j], i):
                    switch = j
                    break

            if switch == None:
                return -1
            else:
                (grid, new_moves) = self.swap(grid, switch, i)
                moves += new_moves

        return moves
