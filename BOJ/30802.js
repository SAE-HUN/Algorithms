const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n')
  .map((el) => el.split(' ').map(Number));

function main() {
  const numberOfParticipants = input.shift()[0];
  const numberOfApplicantsByTshirtSize = input.shift();
  const [bundleOfTshirts, bundleOfPens] = input.shift();

  let minTshirtBundleCount = 0;
  for (const applicants of numberOfApplicantsByTshirtSize) {
    minTshirtBundleCount += Math.ceil(applicants / bundleOfTshirts);
  }
  console.log(minTshirtBundleCount);

  const maxPenBundleCount = Math.floor(numberOfParticipants / bundleOfPens);
  const oneByOnePenCount = numberOfParticipants % bundleOfPens;
  console.log(maxPenBundleCount, oneByOnePenCount);
}

main();
