def dfs(count):
    global answer
    if not count:
        temp = int(''.join(nums))
        if answer < temp:
            answer = temp
        return
    for i in range(length):
        for j in range(i+1, length):
            nums[i], nums[j] = nums[j], nums[i]
            temp_key = ''.join(nums)
            if visited.get((temp_key, count-1), 1):
                visited[(temp_key, count-1)] = 0
                dfs(count-1)
            nums[i], nums[j] = nums[j], nums[i]



T = int(input())
for tc in range(1, T + 1):
    answer = -1
    num, n = input().split()
    nums = list(num)
    n = int(n)
    length = len(nums)
    visited = {}
    dfs(n)
    print(f'#{tc} {answer}')

