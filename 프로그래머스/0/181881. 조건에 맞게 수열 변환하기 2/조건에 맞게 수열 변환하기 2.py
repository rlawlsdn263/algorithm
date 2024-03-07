def solution(arr):
    answer = 0
    # 변화가 없을 때까지 반복
    while True:
        new_arr = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                new_arr.append(num // 2)
            elif num < 50 and num % 2 != 0:
                new_arr.append(num * 2 + 1)
            else:
                new_arr.append(num)
        
        # 변화가 없으면 현재의 반복 횟수를 반환
        if new_arr == arr:
            break
        arr = new_arr
        answer += 1

    # 변화가 시작되지 않는 상태이므로, 모든 숫자가 변화하지 않는 최소 x 값은 0
    return answer