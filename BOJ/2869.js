const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main() {
  const [A, B, V] = input[0];
  let answer = Math.ceil((V - A) / (A - B)) + 1;
  console.log(answer);
}

main();
