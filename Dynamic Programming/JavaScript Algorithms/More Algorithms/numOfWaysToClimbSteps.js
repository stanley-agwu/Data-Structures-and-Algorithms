// Number of ways to climb stairs

/*
How many ways are there to climb stairs if we climb one, two or three steps and want to reach
the fifth step?
*/

// Dynamic Programming Approach

// Recursive solution
const waysToClimbR = (target, ArrOfSteps) => {
  if (target === 0) return 1;
  if (target < 0) return 0;

  let numOfWays = 0;

  for(let num of ArrOfSteps) {
    const remainder = target - num;
    const numWays = waysToClimbR(remainder, ArrOfSteps);
    numOfWays += numWays;
  }
  return numOfWays;
}

// Optimized Recursive solution
const waysToClimbRO = (target, ArrOfSteps, memo = {}) => {
  if (target in memo) return memo[target];
  if (target === 0) return 1;
  if (target < 0) return 0;

  let numOfWays = 0;

  for(let num of ArrOfSteps) {
    const remainder = target - num;
    const numWays = waysToClimbR(remainder, ArrOfSteps, memo);
    numOfWays += numWays;
  }
  memo[target] = numOfWays
  return numOfWays;
}

// Iterative solution
const waysToClimbI = (target, ArrOfSteps) => {
  const table = Array(target + 1).fill(0);

  table[0] = 1;

  for(let i = 0; i <= target; i += 1) {
    if (table[i]) {
      for(let num of ArrOfSteps) {
        table[i + num] += table[i];
      }
    }
  }
  return table[target];
}

console.log(waysToClimbI(5, [1, 1, 2]));
console.log(waysToClimbI(45, [1, 2]));
// console.log(waysToClimbRO(45, [1, 2]));
// console.log(waysToClimbR(5, [1, 2]));