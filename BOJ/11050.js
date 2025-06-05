const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main() {
  const [N, K] = input.pop();
  if (K === 0) {
    console.log(1);
    return;
  }
  if (N === K) {
    console.log(1);
    return;
  }

  const valueOfFactorial = Array.from({ length: N + 1 });
  valueOfFactorial[1] = 1;
  for (let i = 2; i <= N; i++) {
    valueOfFactorial[i] = i * valueOfFactorial[i - 1];
  }

  console.log(
    valueOfFactorial[N] / (valueOfFactorial[N - K] * valueOfFactorial[K])
  );
}

main();
