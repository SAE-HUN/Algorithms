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
  const [n, m, k] = input.shift();
  const candies = input.shift();

  const parents = Array.from({length: n}, (v, k) => k);
  for(const [a, b] of input){
    union(a - 1, b - 1);
  }

  function find(x){
    if(parents[x] != x){
      parents[x] = find(parents[x]);
    }
    return parents[x];
  }

  function union(a, b){
    a = find(a);
    b = find(b);
    if(a > b){
      parents[a] = b;
    } else {
      parents[b] = a;
    }
  }

  const costs = Array.from({length: n}, () => 0);
  const values = Array.from({length: n}, () => 0);
  for(let i = 0; i < n; i++){
    const nodeId = find(i);
    costs[nodeId] += 1;
    values[nodeId] += candies[i];
  }

  const nodes = [];
  for(let i = 0; i < n; i++){
    if(costs[i] == 0) continue;
    nodes.push([values[i], costs[i]]);
  }

  const dp = Array.from({length: k}, () => 0);
  for(let i = 0; i < nodes.length; i++){
    const [v, c] = nodes[i];
    for(let j = k; j >= c; j--){
        dp[j] = Math.max(dp[j], dp[j-c] + v);
    }
  }

  console.log(Math.max(dp[k-1]))
}


main()
