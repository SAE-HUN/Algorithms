const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main() {
  const n = input.shift()[0];
  const numbersToCheckIfPrime = input.shift();

  const MAX_NUMBER = 1000;
  const isPrime = Array.from({ length: MAX_NUMBER + 1 }, () => true);
  isPrime[0] = false;
  isPrime[1] = false;
  for (let number = 2; number <= MAX_NUMBER; number++) {
    if (!isPrime[number]) continue;
    for (let j = 2; number * j <= MAX_NUMBER; j++) {
      isPrime[number * j] = false;
    }
  }

  let answer = 0;
  for (const number of numbersToCheckIfPrime) {
    if (isPrime[number]) answer++;
  }
  console.log(answer);
}

main();
