export function checkPowersOfThree(n: number): boolean {
  const used: Record<number, boolean> = {};
  let rest = n;
  let tmp = n;
  let times = 0;

  while (rest !== 0) {
    if (tmp / 3 >= 1) {
      tmp = (tmp - (tmp % 3)) / 3;
      times++;
    } else {
      if (used[times]) {
        return false;
      } else {
        used[times] = true;
        rest = rest - Math.pow(3, times);
        tmp = rest;
        times = 0;
      }
    }
  }

  return true;
}
