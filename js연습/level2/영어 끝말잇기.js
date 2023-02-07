function solution(n, words) {
  var answer = [];
  let arr = []

  for (let word of words) {
    if (arr.length == 0) {
      arr.push(word)
    } else {
     if (arr.includes(word) || arr.at(-1)[arr.at(-1).length-1] !== word[0]) {
      answer.push(arr.length%n + 1)
      answer.push(Math.floor(arr.length/n)+1)
      break
     } else {
      arr.push(word)
     }
    }
  }
  if (answer.length == 0) {
    answer = [0, 0]
  }

  return answer;
}