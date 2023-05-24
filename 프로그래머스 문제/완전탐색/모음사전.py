from itertools import product
def solution(word):
    alpha = ('a', 'e', 'i', 'o', 'u')
    words = []
    for i in range(1, 6):
        for p in product(alpha, repeat=i):
            words.append(''.join(list(p)))
    words.sort()

    return words.index(word) + 1