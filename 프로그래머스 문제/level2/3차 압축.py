from string import ascii_uppercase

def solution(msg):
    answer = []
    alpha_dict = {}
    count = 1
    for i in ascii_uppercase:
        alpha_dict[i] = count
        count += 1
    while True:
        if msg in alpha_dict:
            answer.append(alpha_dict[msg])
            break
        for i in range(1, len(msg) + 1):
            if msg[0:i] not in alpha_dict:
                answer.append(alpha_dict[msg[0:i-1]])
                alpha_dict[msg[0:i]] = len(alpha_dict) + 1
                msg = msg[i-1:]
                break

    return answer