import { assertEquals } from "@std/assert";

import { shortestCommonSupersequence } from "./main.ts";

Deno.test(function shortestCommonSupersequenceTest() {
  // assertEquals(shortestCommonSupersequence("cab", "abac"), "cabac");
  // assertEquals(shortestCommonSupersequence("abac", "cab"), "cabac");
  assertEquals(
    shortestCommonSupersequence(
      "bcaaacbbbcbdcaddadcacbdddcdcccdadadcbabaccbccdcdcbcaccacbbdcbabb",
      "dddbbdcbccaccbababaacbcbacdddcdabadcacddbacadabdabcdbaaabaccbdaa",
    ),
    "cabac",
  );
});
