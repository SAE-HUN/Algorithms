const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main() {
  const numbersToCheckIfPalindrome = input.flat();
  numbersToCheckIfPalindrome.pop();
  for (const number of numbersToCheckIfPalindrome) {
    const digits = number.toString().split('').map(Number).reverse();
    if (number === Number(digits.join(''))) {
      console.log('yes');
    } else {
      console.log('no');
    }
  }
}

main();
