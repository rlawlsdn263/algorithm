def solution(num_list):
    #짝수 요소들의 합    
    even = sum(num_list[i] for i in range(0, len(num_list), 2))
    #홀수 요소들의 합
    odd = sum(num_list[i] for i in range(1, len(num_list), 2))
    #짝수와 홀수 요소들의 합 중에 더 큰 값을 반환
    return max(even, odd)