function solution(s)
{
  if (s.length % 2 != 0) {
    return 0;
  }
  var answer = -1;
  let stack = [];
  for (let i = 0; i < s.length; i++) {
     if (stack.length == 0) {
      stack.push(s[i])
     } else {
      stack.at(-1) === s[i] ? stack.pop() : stack.push(s[i])
     }
  }

  stack.length == 0 ? answer = 1 : answer = 0

  return answer;
}