import { assertEquals } from "@std/assert";

import { mostProfitablePath } from "./main.ts";

Deno.test.ignore(function constructFromPrePostTest() {
  assertEquals(
    mostProfitablePath(
      [
        [0, 1],
        [1, 2],
        [1, 3],
        [3, 4],
      ],
      3,
      [-2, 4, 2, -4, 6],
    ),
    6,
  );
  assertEquals(
    mostProfitablePath(
      [
        [0, 1],
        [1, 2],
        [2, 3],
      ],
      3,
      [-5644, -6018, 1188, -8502],
    ),
    -11662,
  );
  assertEquals(
    mostProfitablePath(
      [[0,2],[0,4],[1,3],[1,2]],
      1,
      [3958,-9854,-8334,-9388,3410],
    ),
    7368
  );
});
