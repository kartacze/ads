// 2467. Most Profitable Path in a Tree

export class TreeNodeTed {
  val: number;
  left: TreeNodeTed | null;
  right: TreeNodeTed | null;
  am: number;
  parent: TreeNodeTed | null;
  income: number;

  constructor(
    val: number,
    am: number,
    parent: TreeNodeTed | null,
    left?: TreeNodeTed | null,
    right?: TreeNodeTed | null,
  ) {
    this.am = am;
    this.parent = parent;
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
    this.income = 0;
  }
}

export function mostProfitablePath(
  edges: number[][],
  bob: number,
  amount: number[],
): number {
  let bobs_node: TreeNodeTed | null = null;

  const build = (node: TreeNodeTed) => {
    let edge = edges[0];
    if (node.val === bob) {
      bobs_node = node;
    }

    if (edge) {
      if (edge[0] === node.val) {
        node.left = new TreeNodeTed(edge[1], amount.shift() || 0, node);
        edges.shift();
        build(node.left);
      }
    }

    edge = edges[0];

    if (edge) {
      if (edge[0] === node.val) {
        node.right = new TreeNodeTed(edge[1], amount.shift() || 0, node);
        edges.shift();
        build(node.right);
      }
    }

    return node;
  };

  const root = build(new TreeNodeTed(edges[0][0], amount.shift() || 0, null));

  let bobs_path: TreeNodeTed[] = [];

  while (bobs_node !== null) {
    bobs_path.push(bobs_node);
    bobs_node = bobs_node.parent as TreeNodeTed;
  }

  while (bobs_path.length > 0) {
    if (bobs_path.length === 1) {
      bobs_path[0].am = bobs_path[0].am / 2;
      bobs_path = [];
    } else {
      bobs_path.pop();
      const last = bobs_path.shift();
      if (last) {
        last.am = 0;
      }
    }
  }

  const results: number[] = [];

  let arr: TreeNodeTed[] = [root];

  while (arr.length !== 0) {
    arr.forEach((n) => {
      n.income = (n.parent ? n.parent.income : 0) + n.am;
      if (!n.left && !n.right) {
        results.push(n.income);
      }
    });
    arr = arr.flatMap((n) => [n.left, n.right]).filter((n) => !!n);
  }

  return results.reduce((acc, cur) => (cur > acc ? cur : acc), results[0]);
}
