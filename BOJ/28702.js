const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').flat());

function main() {
  const fizzBuzzStrings = input;
  let nextFizzBuzzNumber;
  for (let i = 0; i < fizzBuzzStrings.length; i++) {
    if (isNaN(Number(fizzBuzzStrings[i]))) continue;
    nextFizzBuzzNumber = Number(fizzBuzzStrings[i]) + (3 - i);
  }

  const isMultipleOfThree = nextFizzBuzzNumber % 3 === 0;
  const isMultipleOfFive = nextFizzBuzzNumber % 5 === 0;
  if (isMultipleOfThree && isMultipleOfFive) {
    console.log('FizzBuzz');
  } else if (isMultipleOfThree) {
    console.log('Fizz');
  } else if (isMultipleOfFive) {
    console.log('Buzz');
  } else {
    console.log(nextFizzBuzzNumber);
  }
}

main();
