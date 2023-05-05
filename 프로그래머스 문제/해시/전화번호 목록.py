def solution(phone_book):
    dic = {}
    for p in phone_book:
        dic[p] = 1
    for p in phone_book:
        sen = ""
        for num in p:
            sen += num
            if sen in dic and sen != p:
                return False
    return True