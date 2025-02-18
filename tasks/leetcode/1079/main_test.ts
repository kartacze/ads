import { assertEquals } from "@std/assert";

import { numTilePossibilities } from "./main.ts";

Deno.test(function numTilePossibilitiesTest() {
  assertEquals(numTilePossibilities("AAB"), 8);
  assertEquals(numTilePossibilities("AAABBC"), 188);
  assertEquals(numTilePossibilities("V"), 1);
});
