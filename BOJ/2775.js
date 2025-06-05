const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

function main() {
  const apartment = Array.from({ length: 15 }, () =>
    Array.from({ length: 14 }, () => 0)
  );
  for (let i = 0; i < 14; i++) {
    apartment[0][i] = i + 1;
  }

  for (let i = 1; i <= 14; i++) {
    for (let j = 0; j < 14; j++) {
      for (let k = 0; k <= j; k++) {
        apartment[i][j] += apartment[i - 1][k];
      }
    }
  }

  const T = input[0];
  for (let i = 0; i < T; i++) {
    const k = input[2 * i + 1];
    const n = input[2 * i + 2];
    console.log(apartment[k][n - 1]);
  }
}

main();
