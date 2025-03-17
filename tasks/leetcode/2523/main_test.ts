import { assertEquals } from "@std/assert";

import { closestPrimes } from "./main.ts";

Deno.test(function closestPrimesTest() {
  // assertEquals(closestPrimes(10, 20), [11, 13]);
  // assertEquals(closestPrimes(19, 31), [29, 31]);
  // assertEquals(closestPrimes(84084, 84243), [84101, 84103]);
  // assertEquals(closestPrimes(84084, 407043), [84101, 84103]);
  assertEquals(closestPrimes(341663, 815604), [341771, 341773]);
});
