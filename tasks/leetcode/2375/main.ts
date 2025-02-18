// 2375. Construct Smallest Number From DI String

export function smallestNumber(pattern: string): string {
  const used = Array(10).fill(false);
  used[0] = true;

  const [valid, result] = find("  " + pattern, used, "");

  if (valid) {
    return result;
  }

  return "1";
}

const find = (
  pattern: string,
  used: boolean[],
  str: string,
): [false] | [true, string] => {
  const character = pattern[0];

  if (str !== "" && character !== " ") {
    const first = Number(str[str.length - 2]);
    const last = Number(str[str.length - 1]);

    if (character === "D") {
      if (last > first) {
        return [false];
      }
    }

    if (character === "I") {
      if (last < first) {
        return [false];
      }
    }
  }

  if (pattern.length === 1) {
    return [true, str];
  }

  for (let i = 1; i < 10; i++) {
    if (used[i]) continue;

    const new_used = [...used];
    new_used[i] = true;

    const [valid, result] = find(
      pattern.slice(1, pattern.length),
      new_used,
      `${str}${i}`,
    );

    if (valid) {
      return [valid, result];
    }
  }

  return [false];
};
