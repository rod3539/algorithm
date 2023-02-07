function solution(s) {
  var answer = '';
  let arr = s.split(' ')
  let a = 1000000000;
  let b = -1000000000;
  for (let i = 0; i < arr.length; i++) {
    if (Number(arr[i]) > b) {
      b = Number(arr[i])
    }
    if (Number(arr[i]) < a) {
      a = Number(arr[i])
    }
    console.log(a, b)
  }
  answer = String(a) + ' ' + String(b)
  return answer;
}