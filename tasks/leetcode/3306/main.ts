const vowels = ["a", "i", "e", "o", "u"];

const hasAllVowels = (counter: Record<string, number>) => {
  for (let i = 0; i < vowels.length; i++) {
    if (counter[vowels[i]] === 0) {
      return false;
    }
  }

  return true;
};

const getCount = (
  word: string,
  left: number,
  counter: Record<string, number>,
) => {
  const ctr = { ...counter };
  let total = 0;
  let canCount = hasAllVowels(counter);
  let c_left = left;

  while (canCount) {
    const letter = word[c_left];
    if (isVowel(letter)) {
      ctr[letter] = ctr[letter] - 1;
      canCount = hasAllVowels(ctr);
    } else {
      canCount = false;
    }
    c_left++;
    total += 1;
  }

  return total;
};

const isVowel = (str: string) => vowels.includes(str);

export function countOfSubstrings(word: string, k: number): number {
  let total = 0;

  const counter = {
    a: 0,
    o: 0,
    e: 0,
    i: 0,
    u: 0,
  };

  let left = 0;
  let right = 0;
  const cons: number[] = [];

  while (right < word.length) {
    const next = word[right];
    const vowel = isVowel(next);

    // console.log("position: ", left, right, word[left], word[right]);

    if (!vowel && !cons.includes(right)) {
      cons.push(right);
    } else {
      // @ts-ignore some comment
      counter[next] += 1;
    }

    // console.log("state: ", counter, cons);

    if (cons.length === k && hasAllVowels(counter)) {
      // console.log(getCount(counter));
      const count = getCount(word, left, counter);
      total += count;
      // console.log("TOTAL ADDDDED", total, count, cons);
    }

    if (cons.length > k) {
      const next_left = (cons.shift() || left) + 1;
      // Recalculate counter
      for (let i = left; i < next_left - 1; i++) {
        // console.log("clearing i ", i, word[i]);
        // @ts-ignore some comment
        counter[word[i]] = counter[word[i]] - 1;
      }

      left = next_left;
      // if (!isVowel(word[next_left])) {
      //   right++;
      // }
      if (next_left - 1 === right) {
        right++;
      }

      // console.log("NEXT LEFT", next_left);

      // console.log("COUNTER CLEARED", counter);
    } else {
      right++;
    }
  }

  return total;
}
