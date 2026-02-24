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
