import { assertEquals } from "@std/assert";

import { checkPowersOfThree } from "./main.ts";

Deno.test(function checkPowersOfThreeTest() {
  assertEquals(checkPowersOfThree(11), false);
  assertEquals(checkPowersOfThree(12), true);
  assertEquals(checkPowersOfThree(91), true);
  assertEquals(checkPowersOfThree(21), false);
});
