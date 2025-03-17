// 889. Construct Binary Tree from Preorder and Postorder Traversal

// Definition for a binary tree node.
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

export function constructFromPrePost(
  preorder: number[],
  postorder: number[],
): TreeNode | null {
  const makeNode = (): TreeNode | null => {
    const node = new TreeNode(preorder.shift());

    if (node.val !== postorder[0]) {
      node.left = makeNode();
    }

    if (node.val !== postorder[0]) {
      node.right = makeNode();
    }

    if (node.val === postorder[0]) {
      postorder.shift();
      return node;
    }

    return node;
  };

  return makeNode();
}
