import { assertEquals } from "@std/assert";

import { ProductOfNumbers } from "./main.ts";

Deno.test(function removeOccurrencesTest1() {
  const productOfNumbers = new ProductOfNumbers();
  productOfNumbers.add(3); // [3]
  productOfNumbers.add(0); // [3,0]
  productOfNumbers.add(2); // [3,0,2]
  productOfNumbers.add(5); // [3,0,2,5]
  productOfNumbers.add(4); // [3,0,2,5,4]
  assertEquals(productOfNumbers.getProduct(2), 20);
  assertEquals(productOfNumbers.getProduct(3), 40);
  assertEquals(productOfNumbers.getProduct(4), 0);
  productOfNumbers.add(8); // [3,0,2,5,4,8]
  assertEquals(productOfNumbers.getProduct(2), 32);
});
