const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  console.log((!(line % 4) && line % 100) || !(line % 400) ? 1 : 0);
});
