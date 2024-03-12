def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {x: dice.count(x) for x in set(dice)}
    
    # 네 주사위 숫자가 모두 같은 경우
    if len(counts) == 1:
        p = dice[0]
        return 1111 * p
    # 세 주사위 숫자가 같은 경우
    elif 3 in counts.values():
        p = max(counts, key=counts.get)
        q = min(set(dice) - {p})
        return (10 * p + q) ** 2
    # 두 개씩 같은 값이 나오는 경우
    elif len(counts) == 2 and all(value == 2 for value in counts.values()):
        p, q = counts.keys()
        return (p + q) * abs(p - q)
    # 두 주사위가 같고 나머지 두 주사위가 다른 경우
    elif 2 in counts.values() and len(counts) == 3:
        p = [key for key, value in counts.items() if value == 2][0]
        q, r = set(dice) - {p}
        return q * r
    # 모두 다른 숫자가 나오는 경우
    else:
        return min(dice)