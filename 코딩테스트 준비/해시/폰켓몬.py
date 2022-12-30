def solution(nums):
    num_list = []
    for num in nums:
        if len(num_list) >= len(nums) / 2:
            break
        if not num in num_list:
            num_list.append(num)

    return len(num_list)