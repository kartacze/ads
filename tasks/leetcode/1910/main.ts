// 1910. Remove All Occurrences of a Substring
//

export function removeOccurrences(s: string, part: string): string {
  const reversedPart = part.split("").reverse().join("");
  let stack = "";
  const str = s.split("");

  while (str.length !== 0) {
    const letter = str.shift();
    if (letter) {
      stack = letter + stack;

      while (stack.startsWith(reversedPart)) {
        stack = stack.slice(part.length);
      }
    }
  }

  return stack.split("").reverse().join("");
}
