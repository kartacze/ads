import { assertEquals } from "@std/assert";

import { constructDistancedSequence } from "./main.ts";

Deno.test.ignore(function constructDistancedSequenceTest() {
  // assertEquals(constructDistancedSequence(3), [3, 1, 2, 3, 2]);
  assertEquals(constructDistancedSequence(5), [5, 3, 1, 4, 3, 5, 2, 4, 2]);
});
