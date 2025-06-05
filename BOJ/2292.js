const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main() {
  let n = input.shift()[0];
  n--;
  let answer = 1;
  while (n > 0) {
    n -= 6 * answer;
    answer++;
  }

  console.log(answer);
}

main();
