function solution(k, tangerine) {
  const obj = {};
  tangerine.forEach((n) => {
    obj[n] = ++obj[n] || 1
  })
  let i = 0;
  let answer = 0;
  let arr = Object.values(obj).sort((a, b) => b-a);
  for (o of arr) {
    i += o;
    answer += 1
    if (i >= k) {
      break
    }
  }
  return answer;
}