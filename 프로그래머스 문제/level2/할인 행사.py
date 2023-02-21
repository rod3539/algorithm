def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        a = discount[i:i + 10]
        b = 0
        for j in range(len(number)):
            if a.count(want[j]) == number[j]:
                b += 1
            else:
                break
        if b == len(number):
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))