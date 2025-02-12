function solution(input) {
  const [n, m] = input.shift().split(" ").map(Number);
  const board = input.map((line) => line.split(" ").map(Number));

  const dp = Array.from(Array(n), () => Array(m).fill(-Infinity));

  const suffixSum = Array(m + 1).fill(0);
  for (let i = 1; i < m + 1; i++) {
    suffixSum[i] = suffixSum[i - 1] + board[0][i - 1];
  }
  dp[0] = suffixSum.slice(1);

  for (let i = 1; i < n; i++) {
    const rightMax = [...dp[i]];
    const leftMax = [...dp[i]];

    rightMax[0] = dp[i - 1][0] + board[i][0];
    leftMax[m - 1] = dp[i - 1][m - 1] + board[i][m - 1];

    for (let j = 1; j < m; j++) {
      rightMax[j] = Math.max(dp[i - 1][j], rightMax[j - 1]) + board[i][j];
      leftMax[m - 1 - j] =
        Math.max(dp[i - 1][m - 1 - j], leftMax[m - j]) + board[i][m - 1 - j];
    }
    dp[i] = dp[i].map((_, j) => Math.max(rightMax[j], leftMax[j]));
  }
  console.log(dp[n - 1][m - 1]);
}

const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  solution(input);
  process.exit();
});
