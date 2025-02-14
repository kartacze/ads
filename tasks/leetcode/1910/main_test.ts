import { assertEquals } from "@std/assert";

import { removeOccurrences } from "./main.ts";

Deno.test(function removeOccurrencesTest1() {
  assertEquals(removeOccurrences("daabcbaabcbc", "abc"), "dab");
  assertEquals(removeOccurrences("axxxxyyyyb", "xy"), "ab");
});
