import { assertEquals } from "@std/assert";

import { smallestNumber } from "./main.ts";

Deno.test(function smallestNumberTest() {
  assertEquals(smallestNumber("DDD"), "4321");
  assertEquals(smallestNumber("IIIDIDDD"), "123549876");
  assertEquals(smallestNumber("I"), "12");
});
