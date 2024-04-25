def solution(nums):
    n = len(nums) // 2
    answer = list(set(nums))

    if len(answer) > n:
        return n
    else:
        return len(answer)