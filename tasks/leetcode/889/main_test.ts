import { assertEquals } from "@std/assert";

import { constructFromPrePost } from "./main.ts";
import { treeToList } from "../../utils/tree_to_list.ts";

Deno.test(function constructFromPrePostTest() {
  assertEquals(
    treeToList(
      constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]),
    ),
    [1, 2, 3, 4, 5, 6, 7],
  );
});
