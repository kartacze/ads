from typing import Optional

from structs.tree_node import TreeNode


class LeetCodeTreeReader:
    def to_node(self, list: list[int | None], top=None) -> Optional[TreeNode]:
        print(list)
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

    def from_node(self, node: Optional[TreeNode]) -> list[int | None]:
        if node == None:
            return [None]

        top = node.val

        left = node.left
        right = node.right

        if left == None and right == None:
            return [top]

        return [top] + self.from_node(left) + self.from_node(right)
