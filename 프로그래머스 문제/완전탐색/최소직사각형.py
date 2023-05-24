def solution(sizes):
    w = 0
    h = 0
    for a, b in sizes:
        if a >= b:
            if a > w:
                w = a
            if b > h:
                h = b
        else:
            if b > w:
                w = b
            if a > h:
                h = a

    return w * h