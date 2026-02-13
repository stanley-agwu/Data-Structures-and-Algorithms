// Make The String Great

/*
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and 
remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.
Input: s = "abBAcC"
Output: ""

Input: s = "leEeetcode"
Output: "leetcode"

Input: s = "s"
Output: "s"
*/

function makeStringGreat(s) {
  let stack = [];

  for (let char of s) {
    const lastStackElement = stack[stack.length - 1];
    if (stack.length && lastStackElement !== char && lastStackElement.toLowerCase() === char.toLowerCase()) {
      stack.pop();
    } else {
      stack.push(char);
    }
    return stack.join('');
  }
}

console.log(makeStringGreat('abBAcC')); // ''
console.log(makeStringGreat('leEeetcode')); // 'leetcode'
console.log(makeStringGreat('s')); // 's'