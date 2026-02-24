from typing import Optional, Tuple

from structs.tree_node import TreeNode
from utils.tree_reader import LeetCodeTreeReader


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        final = []
        stack: list[Tuple[TreeNode, str]] = [(root, "")]
        while stack:
            r, v = stack.pop()
            print("ROOT")
            print(r, v)

            if r.right:
                stack.append((r.right, v + str(r.val)))
            if r.left:
                stack.append((r.left, v + str(r.val)))

            if (not r.left) and (not r.right):
                final.append(v + str(r.val))

        return sum(int(x, 2) for x in final)
