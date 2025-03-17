// 873. Length of Longest Fibonacci Subsequence

export function lenLongestFibSubseq(arr: number[]): number {
  let final_length: number = 0;
  const visited: number[] = new Array(arr.length * arr.length).fill(2);

  for (let s = 0; s < arr.length - 1; s++) {
    for (let e = s + 1; e < arr.length - 1; e++) {
      const sum = arr[s] + arr[e];
      for (let c_index = e + 1; arr[c_index] <= sum; c_index++) {
        if (arr[c_index] === sum) {
          const count = visited[s * arr.length + e];
          if (count + 1 > final_length) {
            final_length = count + 1;
          }
          visited[e * arr.length + c_index] = count + 1;
        }
      }
    }
  }

  return final_length;
}
