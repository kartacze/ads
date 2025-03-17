import { assertEquals } from "@std/assert";

import { TreeNode } from "../types/TreeNode.ts";
import { treeToList } from "./tree_to_list.ts";

Deno.test(function treeToListTest() {
  const node: TreeNode = new TreeNode(
    1,
    new TreeNode(2),
    new TreeNode(3, new TreeNode(4)),
  );
  assertEquals(treeToList(node), [1, 2, 3, 4]);
});
