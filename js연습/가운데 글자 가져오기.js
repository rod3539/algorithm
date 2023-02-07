function solution(s) {
    var answer = '';
    s.length % 2 == 0 ? 
    answer = s.slice(s.length / 2-1, s.length/2+1) : answer = s.substr(Math.floor(s.length/2), 1)
    return answer;
}