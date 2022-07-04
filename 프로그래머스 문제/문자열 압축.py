def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        b = ''
        count = 1
        tmp = s[:i]
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                count += 1
            else:
                if count != 1:
                    b = b + str(count) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j+i]
                count = 1
        if count != 1:
            b = b + str(count) + tmp
        else:
            b = b + tmp
        result.append(len(b))
    return min(result)