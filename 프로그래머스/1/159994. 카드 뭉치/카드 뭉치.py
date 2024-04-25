def solution(cards1, cards2, goal):
    answer = 'Yes'

    for g in goal:
        if cards1 and g in cards1[0]:
            cards1.pop(0)
        elif cards2 and g in cards2[0]:
             cards2.pop(0)
        else:
            answer = 'No'

    return answer