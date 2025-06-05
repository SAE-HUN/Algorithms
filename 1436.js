const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim();

function main() {
  const N = Number(input);
  const titles = [['666']];
  for (let i = 0; i < 5; i++) {
    const previousTitles = titles[titles.length - 1];
    const nextTitles = new Set();

    for (const title of previousTitles) {
      for (let j = 0; j < 10; j++) {
        nextTitles.add(j.toString() + title);
        nextTitles.add(title + j.toString());
      }
    }
    titles.push([...nextTitles]);
  }

  const normalTitles = titles.flat().map(Number);
  const uniqueTitles = [...new Set(normalTitles)];
  const sortedTitles = uniqueTitles.sort((a, b) => a - b);
  console.log(sortedTitles[N - 1]);
}

main();
