/** S = Sum of the length of strings in words[].
 * Time Complexity: O(S)
 * Space Complexity: O(S)
 */
/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function (words) {
  if (words.length === 1) return 1;

  // index array
  let morse = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
  ];

  const set = new Set();

  for (let word of words) {
    let morseWord = "";

    for (let c of word) {
      morseWord += morse[c.charCodeAt(0) - "a".charCodeAt(0)];
    }

    set.add(morseWord);
  }

  return set.size;
};
