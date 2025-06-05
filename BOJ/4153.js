const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main() {
  for (const sides of input) {
    const [a, b, c] = sides.sort((a, b) => a - b);
    if (a === 0 || b === 0 || c === 0) {
      break;
    }
    if (a ** 2 + b ** 2 === c ** 2) {
      console.log('right');
    } else {
      console.log('wrong');
    }
  }
}

main();
