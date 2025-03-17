import { TreeNode } from "../types/TreeNode.ts";

export const treeToList = (node: TreeNode | null) => {
  if (!node) {
    return null;
  }

  const response: number[] = [];
  let arr: TreeNode[] = [node];

  while (arr.length !== 0) {
    arr.forEach((n) => response.push(n.val));
    arr = arr.flatMap((n) => [n.left, n.right]).filter((n) => !!n);
  }

  return response;
};
