class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tree = [[0, poured - 1.0 if poured > 1.0 else poured, 0]]
        for i in range(1, query_row + 1):
            tree.append([0])
            for j in range(1, len(tree[i - 1])):
                diff = tree[i - 1][j - 1] / 2 + tree[i - 1][j] / 2
                tree[i].append(diff - 1.0 if diff > 1.0 else 0.0)
            tree[i].append(0)
        flow = (
            tree[query_row - 1][query_glass] / 2
            + tree[query_row - 1][query_glass + 1] / 2
        )
        return flow if flow <= 1 else 1


def test_champagneTower():
    assert Solution().champagneTower(25, 6, 1) == 0.18750
    assert Solution().champagneTower(2, 1, 1) == 1 / 2
    assert Solution().champagneTower(100000009, 33, 17) == 1.0
    assert Solution().champagneTower(2, 1, 1) == 1 / 2
    assert Solution().champagneTower(1, 1, 1) == 0.0
