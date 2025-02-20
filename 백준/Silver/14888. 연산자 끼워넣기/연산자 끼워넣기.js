const input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
const numbers = input[1].split(" ").map(Number);
const operators = input[2].split(" ").map(Number);

let min = Infinity;
let max = -Infinity;

dfs(numbers[0], 1, operators);

console.log(max || 0);
console.log(min || 0);

function dfs(currentValue, index, operators) {
  if (operators.every((value) => value === 0)) {
    min = Math.min(min, currentValue);
    max = Math.max(max, currentValue);
    return;
  }

  if (operators[0] > 0) {
    operators[0]--;
    dfs(currentValue + numbers[index], index + 1, operators);
    operators[0]++;
  }
  if (operators[1] > 0) {
    operators[1]--;
    dfs(currentValue - numbers[index], index + 1, operators);
    operators[1]++;
  }
  if (operators[2] > 0) {
    operators[2]--;
    dfs(currentValue * numbers[index], index + 1, operators);
    operators[2]++;
  }
  if (operators[3] > 0) {
    operators[3]--;
    dfs(~~(currentValue / numbers[index]), index + 1, operators);
    operators[3]++;
  }
}
