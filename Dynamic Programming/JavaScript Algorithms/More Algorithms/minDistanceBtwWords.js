// Minimum Distance Between Words of a String
/*
Given a string s and two words w1 and w2 that are present in S. 
The task is to find the minimum distance between w1 and w2. Here, 
distance is the number of steps or words between the first and the second word. 
*/

// Uses two pointer solution

const minDistanceBtwWords = (text, w1, w2) => {
  const wordsArr = text.split(' ');
  let minDistance = Infinity;
  let posOfLastWord = -1;
  let posOfFirstWord = -1;

  for(let i = 0; i < wordsArr.length; i += 1) {
    if (wordsArr[i] === w1) {
      posOfFirstWord = i;
      if (posOfLastWord !== -1) {
        minDistance = Math.min(minDistance, Math.abs(posOfLastWord - posOfFirstWord));
      }
    }
    if (wordsArr[i] === w2) {
      posOfLastWord = i;
      if (posOfFirstWord !== -1) {
        minDistance = Math.min(minDistance, Math.abs(posOfLastWord - posOfFirstWord));
      }
    }
  }
  return minDistance === Infinity ? -1 : minDistance - 1;
}

console.log(minDistanceBtwWords('the quick the brown quick brown the frog', 'quick', 'frog'));
console.log(minDistanceBtwWords('the quick brown fox jumps over the lazy dog the quick brown', 'quick', 'dog'));