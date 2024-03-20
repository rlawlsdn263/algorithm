def solution(participant, completion):

    value = 0
    answer = {}

    for part in participant:
        answer[hash(part)] = part # part를 해싱해 key로 넣고, part를 value로 넣는다
        value += int(hash(part)) # value는 part를 해싱한 값을 int로 한다.

    for comp in completion:
        value -= hash(comp)  # comp를 해싱한 값은 part와 동일하다. 고로 모든 값을 제거하면 하나의 해쉬만 남는다. 그게 범인이다.

    return answer[value]