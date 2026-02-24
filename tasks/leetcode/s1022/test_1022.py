from structs.tree_node import TreeNode
from tasks.leetcode.s1022.s1022 import Solution
from utils.tree_reader import LeetCodeTreeReader


def test_sumRootToLeaf():
    s = Solution()
    # root = LeetCodeTreeReader().to_node([1, 0, 1, 0, 1, 0, 1, None, None, None, None])
    root = TreeNode(
        1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1))
    )
    assert s.sumRootToLeaf(root) == 22
