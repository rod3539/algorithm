def solution(numbers):
    input_list = list(map(str, numbers))

    input_list.sort(key=lambda x: x * 3, reverse=True)
    answer = ''
    answer = answer.join(input_list)
    return str(int(answer))