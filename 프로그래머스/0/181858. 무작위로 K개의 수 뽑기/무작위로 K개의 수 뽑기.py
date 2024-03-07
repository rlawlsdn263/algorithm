def solution(arr, k):
    # 중복 제거 후 서로 다른 수만 저장
    unique_nums = []
    for num in arr:
        if num not in unique_nums:
            unique_nums.append(num)
        # 배열의 길이가 k에 도달하면 종료
        if len(unique_nums) == k:
            break
    
    # 완성될 배열의 길이가 k보다 작으면 -1로 채움
    while len(unique_nums) < k:
        unique_nums.append(-1)

    return unique_nums