// 1352. Product of the last k numbers

export class ProductOfNumbers {
  k: number[];
  size: number;

  constructor() {
    this.k = [];
    this.size = 0;
  }

  add(num: number): void {
    if (num === 0) {
      this.size = 0;
      this.k = [];
      return;
    }
    this.size += 1;
    this.k.push(num * (this.k.at(-1) ?? 1));
  }

  getProduct(k: number): number {
    if (k > this.size) {
      return 0;
    }

    return (this.k.at(-1) ?? 0) / (this.k.at(-1 * (k + 1)) ?? 1);
  }
}
