const input = require('fs')
  .readFileSync(
    process.platform === 'linux'
      ? '/dev/stdin'
      : 'input.txt'
  )
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main(){
  const n = input.shift()[0];
  const matrix = input;
  const toRight = matrix.map(row => [...row]);
  const toLeft = matrix.map(row => [...row]);

  for(let i = 0; i < n; i++){
    for(let j = 0; j < n; j++){
      if(i === 0 || j === 0){
        continue;
      }
      toRight[i][j] += toRight[i - 1][j - 1]
    }
  }

  for(let i = 0; i < n; i++){
    for(let j = 0; j < n; j++){
      if(i === 0 || j === n - 1){
        continue;
      }
      toLeft[i][j] += toLeft[i - 1][j + 1]
    }
  }

  let answer = -Infinity;
  for(let i = 0; i < n ; i++){
    for(let j = 0; j < n; j++){
      for(let k = 1; k < n; k++){
        if(i + k >= n || j + k >= n){
          continue;
        }

        const primaryFrom = i === 0 || j === 0 ? 0 : toRight[i - 1][j - 1];
        const primaryTo = toRight[i + k][j + k];
        const primary = primaryTo - primaryFrom;
        const secondaryFrom = i === 0 || j + k >= n - 1 ? 0 : toLeft[i - 1][j + k + 1];
        const secondaryTo = toLeft[i + k][j];
        const secondary = secondaryTo - secondaryFrom;
        answer = Math.max(answer, primary - secondary)
      }
    }
  }

  console.log(answer);
}

main()
