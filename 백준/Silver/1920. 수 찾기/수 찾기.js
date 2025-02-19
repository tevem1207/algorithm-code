const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", function init(line) {
  input.push(line);
  if (input.length === 4) {
    rl.close();
    processInput(input);
  }
});

function processInput(input) {
  const A = input[1].split(" ").map(Number);
  const arr = input[3].split(" ").map(Number);

  const setA = new Set(A);

  arr.forEach((num) => console.log(Number(setA.has(num))));
}
