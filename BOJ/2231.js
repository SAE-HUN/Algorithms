const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main() {
  const n = input.shift()[0];
  const minConstructorCandidates = n - 9 * n.toString().length;
  const constructorCandidates = Array.from(
    { length: n - minConstructorCandidates },
    (_, i) => i + minConstructorCandidates
  );

  for (const candidate of constructorCandidates) {
    const decompositionSum = candidate
      .toString()
      .split('')
      .map(Number)
      .reduce((a, b) => a + b, candidate);
    if (decompositionSum === n) {
      console.log(candidate);
      return;
    }
  }

  console.log(0);
}

main();
