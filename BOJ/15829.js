const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' '));

function main() {
  const string = input.pop()[0];
  const L = input.pop()[0];
  const r = 31n;
  const M = 1234567891n;

  let answer = 0n;
  for (let i = 0; i < L; i++) {
    const a = string[i].charCodeAt() - 96;
    answer += BigInt(a) * r ** BigInt(i);
    answer %= M;
  }

  console.log(answer.toString());
}

main();
