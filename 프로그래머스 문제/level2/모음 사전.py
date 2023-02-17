from itertools import product
def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1, 6):
        for p in product(arr, repeat=i):
            words.append(''.join(list(p)))
    words.sort()
    return words.index(word) + 1

print(solution('AAAA'))