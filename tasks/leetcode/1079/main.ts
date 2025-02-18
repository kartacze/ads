// 1079. Letter Tile Possibilities

export function numTilePossibilities(tiles: string): number {
  const mem = {};
  const used = {};

  const result = getThem("", mem, used, tiles);

  return result;
}

const getThem = (
  base: string,
  mem: Record<string, number>,
  used: Record<string, boolean>,
  tiles: string,
): number => {
  // if (used[tiles]) {
  //   return 0;
  // }

  let res = 0;

  for (let i = 0; i < tiles.length; i++) {
    const letter = tiles[i];
    const rest = tiles.slice(0, i) + tiles.slice(i + 1, tiles.length);

    if (!used[base + letter]) {
      used[base + letter] = true;
      if (rest.length !== 0) {
        if (!mem[rest]) {
          const other_response = getThem(base + letter, mem, used, rest);
          mem[rest] = other_response;
        }
        res += mem[rest];
      }
      res += 1;
    }
  }

  return res;
};
