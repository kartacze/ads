// 1718. Construct the Lexicographically Largest Valid Sequence

export function constructDistancedSequence(n: number): number[] {
  const total_lenght = 2 * (n - 1) + 1;
  const array = Array(total_lenght).fill(0);
  const used = Array(n + 1).fill(false);

  const [valid, result] = backtrack(array, n, used, 0);

  if (valid) {
    return result;
  }

  return [0];
}

const backtrack = (
  result: number[],
  n: number,
  used: boolean[],
  index: number,
): [false] | [true, number[]] => {
  while (index < result.length && result[index] !== 0) {
    index++;
  }

  if (index >= result.length) {
    return [true, result];
  }

  for (let i = n; i >= 1; i--) {
    if (used[i]) continue;

    if (i === 1) {
      const old = [...result];
      const oldUsed = [...used];
      result[index] = 1;
      used[1] = true;

      const [valid, newResult] = backtrack(result, n, used, index + 1);

      if (valid) {
        return [valid, newResult];
      }

      result = old;
      used = oldUsed;
    } else if (result[index] === 0 && result[index + i] === 0) {
      const old = [...result];
      const oldUsed = [...used];

      result[index] = i;
      result[index + i] = i;
      used[i] = true;

      const [valid, newResult] = backtrack(result, n, used, index + 1);

      if (valid) {
        return [valid, newResult];
      }

      result = old;
      used = oldUsed;
    }
  }

  return [false];
};
