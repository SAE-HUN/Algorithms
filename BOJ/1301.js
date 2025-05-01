const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : './input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main(){
  function beadsToIndex(beads){
    let index = 0;
    for(let i = 0; i < n; i++){
      count = beads[i];
      index += count * 11 ** (n - i - 1);
    }

    return index;
  }

  function indexToBeads(index){
    const beads = [];
    for(let i = 0; i < n; i++){
      const count  = Math.floor(index / 11 ** (n - i - 1));
      index -= count * 11 ** (n - i - 1);
      beads.push(count);
    }

    return beads
  }

  function indexToBeadType(index){
    const typeA = Math.floor(index / 10);
    const typeB = index - 10 * typeA;
    return [typeA, typeB];
  }

  function beadTypeToIndex(beadType){
    return 10 * beadType[0] + beadType[1];
  }

  const n = input.shift()[0];
  const beads = input.flat();
  const dp = Array.from({length: 50}, () => Array.from({length: 11 ** (n)}, () => -1))
  
  function dfs(typeIndex, beadsIndex){
    if(beadsIndex === 0){
      return 1;
    }

    if(dp[typeIndex][beadsIndex] !== -1){
      return dp[typeIndex][beadsIndex]
    }
    
    let result = 0;
    const beadType = indexToBeadType(typeIndex);
    const beads = indexToBeads(beadsIndex);
    for(let i = 0; i < n; i++){
      if(beadType.includes(i)) continue;
      if(beads[i] === 0) continue;
      beads[i] -= 1;
      result += dfs(beadTypeToIndex([i, beadType[0]]), beadsToIndex(beads))
      beads[i] += 1;
    }

    dp[typeIndex][beadsIndex] = result;
    return result;
  }

  let answer = 0;
  for(let i = 0; i < n; i++){
    for(let j = 0; j < n; j++){
      if(i === j) continue;
      for(let k = 0; k < n; k++){
        if(i === k || j === k) continue;
        if(beads[i] === 0 || beads[j] === 0 || beads[k] === 0) continue;
        beads[i] -= 1;
        beads[j] -= 1;
        beads[k] -= 1;
        const result = dfs(beadTypeToIndex([i, j]), beadsToIndex(beads))
        answer += result
        beads[i] += 1;
        beads[j] += 1;
        beads[k] += 1;
      }
    }
  }

  console.log(answer);
}


main()
