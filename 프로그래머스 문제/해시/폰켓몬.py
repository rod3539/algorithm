def solution(nums):
    nums_set = set(nums)
    answer = 0
    if len(nums_set) > len(nums) / 2:
        answer = int(len(nums) / 2)
    else:
        answer = int(len(nums_set))
    return answer

print(solution([3,1,2,3]))