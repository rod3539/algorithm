def solution(array, commands):
    answer = []
    for command in commands:
        array_list = sorted(array[command[0]-1:command[1]])
        answer.append(array_list[command[2] - 1])
    return answer