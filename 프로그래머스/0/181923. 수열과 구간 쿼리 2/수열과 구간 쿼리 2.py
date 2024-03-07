def solution(arr, queries):
    answer = []

    for q in queries:
        s, e, k = q
        # arr의 부분 배열에서 k보다 큰 수들만 필터링
        filtered = [num for num in arr[s:e+1] if num > k]
        
        # 필터링된 수가 있으면 그 중 최소값을, 없으면 -1을 answer에 추가
        if filtered:
            answer.append(min(filtered))
        else:
            answer.append(-1)

    return answer