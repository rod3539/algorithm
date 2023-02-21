def solution(nums):
    answer = 0
    po_dic = {}
    for num in nums:
        if num not in po_dic.keys():
            po_dic[num] = 1
        else:
            po_dic[num] += 1
    if len(po_dic) >= len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len(po_dic)
    return answer
