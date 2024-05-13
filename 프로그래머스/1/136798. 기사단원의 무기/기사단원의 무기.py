def get_divisor_count(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def solution(number, limit, power):
    total_iron = 0
    for i in range(1, number + 1):
        count = get_divisor_count(i)
        if count > limit:
            total_iron += power
        else:
            total_iron += count
    return total_iron