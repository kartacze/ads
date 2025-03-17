// 1261. Find Elements in a Contaminated Binary Tree

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

type TreeNode = {
  val: number | null;
  left: TreeNode | null;
  right: TreeNode | null;
};

export class FindElements {
  values: number[];

  constructor(root: (number | null)[]) {
    this.values = construct_tree(root);
  }

  find(target: number): boolean {
    return this.values.includes(target);
  }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * var obj = new FindElements(root)
 * var param_1 = obj.find(target)
 */

const get_n_depth_nodes = (
  depth: number,
  current_depth: number,
  node: TreeNode,
): TreeNode[] => {
  if (depth === current_depth) {
    return [node];
  }

  return [
    ...(node.left
      ? get_n_depth_nodes(depth, current_depth + 1, node.left)
      : []),
    ...(node.right
      ? get_n_depth_nodes(depth, current_depth + 1, node.right)
      : []),
  ];
};

const construct_tree = (arr: (number | null)[]): number[] => {
  const values: number[] = [0];

  const root: TreeNode = {
    val: 0,
    left: arr[1] === null ? null : { val: 1, left: null, right: null },
    right: arr[2] === null ? null : { val: 2, left: null, right: null },
  };

  let index = 1;

  for (let depth = 0; depth < 100; depth++) {
    if (index >= arr.length) break;

    for (const node of get_n_depth_nodes(depth, 0, root)) {
      if (index >= arr.length) break;
      const left_value = arr[index] !== null ? 2 * (node.val || 0) + 1 : null;
      index++;
      const right_value =
        index < arr.length && arr[index] !== null
          ? 2 * (node.val || 0) + 2
          : null;
      index++;

      if (left_value) {
        values.push(left_value);
      }

      if (right_value) {
        values.push(right_value);
      }

      node.left = left_value
        ? {
            val: left_value,
            left: {
              val: -1,
              left: null,
              right: null,
            },
            right: {
              val: -1,
              left: null,
              right: null,
            },
          }
        : null;

      node.right = right_value
        ? {
            val: right_value,
            left: {
              val: -1,
              left: null,
              right: null,
            },
            right: {
              val: -1,
              left: null,
              right: null,
            },
          }
        : null;
    }
  }

  return values;
};
