const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
});

rl.on("close", () => {
  const [m, n] = input[0].split(" ").map(Number);
  const grid = Array.from({ length: m }, () => Array(n).fill(0));

  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  const dfs = (x, y, mark) => {
    let area = 1;
    grid[y][x] = mark;
    dir.forEach(([dx, dy]) => {
      if (x + dx >= 0 && x + dx < n && y + dy >= 0 && y + dy < m) {
        if (!grid[y + dy][x + dx]) {
          area += dfs(x + dx, y + dy, mark);
        }
      }
    });
    return area;
  };

  input.slice(1).forEach((line) => {
    const [x1, y1, x2, y2] = line.split(" ").map(Number);
    for (i = y1; i < y2; i++) {
      for (j = x1; j < x2; j++) {
        grid[i][j] = 1;
      }
    }
  });

  let count = 1;
  const result = [];
  for (i = 0; i < m; i++) {
    for (j = 0; j < n; j++) {
      if (!grid[i][j]) {
        result.push(dfs(j, i, count));
        count++;
      }
    }
  }

  console.log(result.length);
  console.log(result.sort((a, b) => a - b).join(" "));
});
