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
  let [N, M, K, t] = input.shift();
  const mold = input.splice(0, M);
  const check = input.slice(0, K);

  const visited = Array.from({length: N + 1}, () => Array.from({length: N + 1}, () => Array.from({length: 2}, () => false)))
  const delta = [
    [-2, -1],
    [-2, 1],
    [-1, -2],
    [-1, 2],
    [1, -2],
    [1, 2],
    [2, -1],
    [2, 1],
  ]

  let queue = [];
  for(const [x, y] of mold){
    queue.push([x, y]);
  }

  for(let day = 0; day < t; day++){
    const nextDay = day + 1;
    const newQueue = []
    while(queue.length){
      const [x, y] = queue.pop();
      for(const [dx, dy] of delta){
        const [nx, ny] = [x + dx, y + dy];
        if(nx > N || ny > N) continue;
        if(nx < 1 || ny < 1) continue;
        if(visited[nx][ny][nextDay % 2]) continue;
        visited[nx][ny][nextDay % 2] = true;
        newQueue.push([nx, ny]);
      }
    }
    queue = newQueue;
  }

  let result = false;
  for(const [x, y] of check){
    if(visited[x][y][t % 2]){
      result = true;
      break;
    }
  }

  if(result){
    console.log("YES")
  } else {
    console.log("NO");
  }
}


main()
