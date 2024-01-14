def solution(num_list):
    # 모든 원소들의 곱을 계산합니다.
    product = 1
    for num in num_list:
        product *= num

    # 모든 원소들의 합을 계산합니다.
    total_sum = sum(num_list)

    # 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1, 그렇지 않으면 0을 반환합니다.
    return 1 if product < total_sum ** 2 else 0