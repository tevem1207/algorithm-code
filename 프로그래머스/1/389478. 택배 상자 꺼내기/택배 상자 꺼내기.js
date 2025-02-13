function solution(n, w, num) {
    const [topRow, topCol] = [getRow(n, w), getCol(n, w)];
    const [targetRow, targetCol] = [getRow(num, w), getCol(num, w)];
    if ((topRow % 2) ? targetCol < topCol : targetCol > topCol) {
        return getRow(n, w) - getRow(num, w);
    }
    return getRow(n, w) - getRow(num, w) + 1;
}

const getRow = (n, w) => Math.ceil(n / w) - 1;
const getCol = (n, w) => getRow(n, w) % 2 ? w - 1 - ((n - 1) % w) : ((n - 1) % w);