export function closestPrimes(left: number, right: number): number[] {
  const primes: number[] = [3, 5, 7];
  const response: number[] = [];

  const abs = Math.abs(right / 2);
  const max_i = abs > left - 1 ? left - 1 : abs;

  forLoop: for (let i = 9; i <= max_i; i += 2) {
    for (const prime of primes) {
      if (i % prime === 0) {
        continue forLoop;
      }
    }

    primes.push(i);
  }

  const a_l = left % 2 === 0 ? left + 1 : left;

  mainLoop: for (let i = a_l; i <= right; i += 2) {
    for (const prime of primes) {
      if (i % prime === 0) {
        continue mainLoop;
      }
    }

    if (i - (response[response.length - 1] || 0) === 2) {
      return [response[response.length - 1], i];
    }

    response.push(i);
  }

  if (response.length < 2) {
    return [-1, -1];
  }

  let smallest_diff = response[1] - response[0];
  let smallest_numbers = [response[0], response[1]];

  for (let i = 1; i < response.length - 1; i++) {
    if (response[i + 1] - response[i] < smallest_diff) {
      smallest_diff = response[i + 1] - response[i];
      smallest_numbers = [response[i], response[i + 1]];
    }
  }

  return smallest_numbers;
}
