export function shortestCommonSupersequence(
  str1: string,
  str2: string,
): string {
  let response: string = str1 + str2;
  const memory: Record<string, boolean> = {};
  const mem2: Record<string, Record<string, string>> = {};

  const find = (str1: string, str2: string, cur: string) => {
    console.log("find", str1, str2, cur);
    console.log("response", response);

    if (
      mem2[str1] &&
      mem2[str1][str2] &&
      mem2[str1][str2].length < cur.length
    ) {
      return;
    } else {
      if (!mem2[str1]) {
        mem2[str1] = {};
      }
    }

    if (memory[cur]) {
      // console.log("IN MEMORY", str1, str2, cur);
      return;
    } else {
      memory[cur] = true;
    }

    if (str1 === "" && str2 === "") {
      if (response.length > cur.length) {
        response = cur;
      }
      return;
    }

    if (str1 === "" && str2 !== "") {
      return find(str1, "", cur + str2);
    }

    if (str2 === "" && str1 !== "") {
      return find("", "", cur + str1);
    }

    if (str1[0] === str2[0]) {
      const letter = str1[0];
      return find(str1.slice(1), str2.slice(1), cur + letter);
    }

    const l1 = str1[0];

    // push to the response and find new_used
    find(str1.slice(1), str2, cur + l1);
    const l2 = str2[0];

    find(str1, str2.slice(1), cur + l2);
  };

  find(str1, str2, "");

  return response;
}
