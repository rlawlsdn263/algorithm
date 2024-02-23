def solution(arr):
    n = len(arr)
    power_of_two = 1
    while power_of_two < n:
        power_of_two *= 2
    zeros_to_add = power_of_two - n
    return arr + [0] * zeros_to_add