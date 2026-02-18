from typing import Optional, List, Tuple
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return (
            "TreeNode{val: "
            + str(self.val)
            + ", left: "
            + str(self.left)
            + ", right: "
            + str(self.right)
            + " }"
        )


class LeetCodeTreeReader:
    def to_node(self, list: List[int | None], top=None) -> Optional[TreeNode]:
        val = top or list.pop(0)

        if val == None:
            return None
        left = None if not list else list.pop(0)
        right = None if not list else list.pop(0)

        if left == None:
            left_node = None
        else:
            left_node = self.to_node(list, left)

        if right == None:
            right_node = None
        else:
            right_node = self.to_node(list, right)

        node = TreeNode(val, left_node, right_node)
        return node

    def from_node(self, node: Optional[TreeNode]) -> List[int | None]:
        if node == None:
            return [None]

        top = node.val

        left = node.left
        right = node.right

        if left == None and right == None:
            return [top]

        return [top] + self.from_node(left) + self.from_node(right)


class Solution:
    def from_node(self, node: Optional[TreeNode]) -> List[int]:
        if node == None:
            return []

        top = node.val

        left = node.left
        right = node.right

        if left == None and right == None:
            return [top]

        return [top] + self.from_node(left) + self.from_node(right)

    def balance(self, items: List[int]) -> Optional[TreeNode]:
        m_index = math.floor(len(items) / 2)
        middle = items[m_index]
        left_items = items[0:m_index]
        right_items = items[m_index + 1 : len(items)]

        return TreeNode(
            middle,
            None if not left_items else self.balance(left_items),
            None if not right_items else self.balance(right_items),
        )

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        items = self.from_node(root)
        node = self.balance(items)

        return node


def test_balanceBST():
    input = [1, None, 2, None, 3, None, 4, None, None]
    output = [2, 1, 3, None, None, None, 4]
    tree = LeetCodeTreeReader().to_node(input)
    result = Solution().balanceBST(tree)
    assert LeetCodeTreeReader().from_node(result) == output

    # input: List[int | None] = [2, 1, 3]
    #
    # tree = LeetCodeTreeReader().to_node(input)
    # print(LeetCodeTreeReader().from_node(tree))
    #
    # assert Solution().balanceBST(tree) == [2, 1, 3]
