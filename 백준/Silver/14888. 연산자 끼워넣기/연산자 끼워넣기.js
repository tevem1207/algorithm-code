const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
let min = Infinity;
let max = -Infinity;

rl.on("line", (line) => input.push(line)).on("close", () => {
  const numbers = input[1].split(" ").map(Number);
  const operators = input[2].split(" ").map(Number);

  dfs(numbers[0], 1, operators);

  console.log(max || 0);
  console.log(min || 0);
});

function dfs(currentValue, index, operators) {
  if (operators.every((value) => value === 0)) {
    min = Math.min(min, currentValue);
    max = Math.max(max, currentValue);
    return;
  }

  const nextNum = parseInt(input[1].split(" ")[index]);

  if (operators[0] > 0) {
    operators[0]--;
    dfs(currentValue + nextNum, index + 1, operators);
    operators[0]++;
  }
  if (operators[1] > 0) {
    operators[1]--;
    dfs(currentValue - nextNum, index + 1, operators);
    operators[1]++;
  }
  if (operators[2] > 0) {
    operators[2]--;
    dfs(currentValue * nextNum, index + 1, operators);
    operators[2]++;
  }
  if (operators[3] > 0) {
    operators[3]--;
    dfs(
      currentValue < 0
        ? -Math.floor(-currentValue / nextNum)
        : Math.floor(currentValue / nextNum),
      index + 1,
      operators
    );
    operators[3]++;
  }
}
