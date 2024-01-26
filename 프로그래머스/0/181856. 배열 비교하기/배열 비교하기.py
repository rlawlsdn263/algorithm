def solution(arr1, arr2):

    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    elif len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        elif sum(arr1) == sum(arr2):
            return 0

# arr1이 더 크면 1
# arr2가 더 크면 -1
# arr1과 arr2가 같으면 0

