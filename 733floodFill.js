/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 * Time complexity - O(N) - N === number of images in screen
 * Space complexity - O(N) - N === size of call stack
 */
var floodFill = function (image, sr, sc, color) {
  const ogColor = image[sr][sc];
  const totRow = image.length;
  const totCol = image[0].length;
  if (ogColor === color) return image;

  function dfs(row, col) {
    if (image[row][col] !== ogColor) return;

    // check self
    image[row][col] = color;

    // add t, r, b, l to q
    if (row >= 1) dfs(row - 1, col);
    if (row + 1 < totRow) dfs(row + 1, col);
    if (col >= 1) dfs(row, col - 1);
    if (col + 1 < totCol) dfs(row, col + 1);
  }
  dfs(sr, sc);
  return image;
};
